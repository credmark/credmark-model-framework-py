# pylint: disable=locally-disabled, unused-import, unused-variable
import importlib
import sys
from typing import List
from datetime import datetime, date, timezone, timedelta
import IPython

import os
import logging
import yaml

from web3.exceptions import ABIFunctionNotFound
from credmark.cmf.engine.model_loader import ModelLoader
from credmark.cmf.engine.model_api import ModelApi

from credmark.cmf.model import Model
from credmark.cmf.model.errors import ModelDataError, ModelRunError
from credmark.cmf.model.print import print_manifest_description
from credmark.cmf.types import (
    Address,
    Account, Contract, Token,
    Accounts, Contracts, Tokens,
    Portfolio, Position,
    Price, PriceList,
    BlockNumber,
    NativeToken,
    NativePosition,
    TokenPosition,
    ContractLedger,
)

from credmark.dto import DTO, DTOField, EmptyInput, IterableListGenericDTO, PrivateAttr

from credmark.cmf.types.ledger import (BlockTable, ContractTable,
                                       LogTable,
                                       ReceiptTable, TokenTable,
                                       TokenTransferTable, TraceTable,
                                       TransactionTable)


# pylint: disable= too-many-arguments
def get_dt(year, month, day, hour=0, minute=0, second=0, microsecond=0):
    return datetime(year, month, day, hour, minute, second, microsecond, tzinfo=timezone.utc)


def get_block(in_dt):
    return BlockNumber.from_timestamp(in_dt.replace(tzinfo=timezone.utc).timestamp())


@Model.describe(slug='console',
                version='1.0',
                display_name='Console',
                description='Credmark Model REPL')
class ConsoleModel(Model):

    console_yaml_path = 'credmark_dev_console.yaml'

    blocks: List[BlockNumber] = []

    # filled in lazily
    _model_manifest_map = {}
    _added_deployed_manifests = False

    def init(self):
        self.load_config(globals())

    def load_config(self, var_namespace):
        path = self.console_yaml_path
        if os.path.isfile(path):
            with open(path, 'r') as fp:
                try:
                    self.logger.debug(f'Loading console config {path}')
                    config = yaml.safe_load(fp)
                    self._process_config(config, var_namespace)
                except Exception as exc:
                    self.logger.error(
                        f'Error loading console config yaml file {path}: {exc}')

    def _process_config(self, config, var_namespace):
        imports = config.get('imports')
        if imports:
            module_imports = imports.get('modules')
            if module_imports:
                for mod_def in module_imports:
                    try:
                        name = mod_def['name']
                        self._import_module(name, mod_def.get('as', name), var_namespace)
                    except KeyError:
                        self.logger.error(
                            f'Error importing module {mod_def} from console config: Missing name')

            global_imports = imports.get('globals')
            if global_imports:
                # a list of module.names.var
                for path in global_imports:
                    self._import_module_global(path, var_namespace)

    def _import_module(self, module_name, name, var_namespace):
        try:
            var_namespace[name] = importlib.import_module(module_name)
        except Exception as exc:
            self.logger.error(f'Error importing {module_name} from console config: {exc}')

    def _import_module_global(self, path, var_namespace):
        try:
            parts = path.split('.')
            name = parts[-1]
            module = importlib.import_module('.'.join(parts[:-1]))
            var_namespace[name] = vars(module)[name]
        except Exception as exc:
            self.logger.error(f'Error importing {path} from console config: {exc}')

    def help(self):
        print('# Credmark model utility shortcuts')
        print('ledger = self.context.ledger')
        print('run_model = self.context.run_model'
              '(model_slug, input=EmptyInput(), return_type=dict): run a model')
        print(
            'run_model_historical = self.context.historical.run_model_historical'
            '(model_slug, model_input, model_return_type, window, interval, '
            ' end_timestamp, snap_clock, model_version)')
        print(
            'run_model_historical_blocks = self.context.run_model_historical_blocks'
            '(model_slug, model_input, model_return_type, window, interval, '
            ' end_block, snap_block, model_version)')
        print('models = self.context.models')
        print('block_number = self.context.block_number')
        print('chain_id = self.context.chain_id')
        print('web3 = self.context.web3')
        print('')
        print('# Utility functions')
        print('list_models(): List available models')
        print('describe_model(slug): Describe a model by slug')
        print('get_dt(y,m,d,h=0,m=0,s=0,ms=0): create UTC datetime')
        print('get_block(timestamp): get the block number before the timestamp')
        print('')
        print('# Console functions')
        print('self.where(): where you are in the chain of blocks')
        print('self.save("output_filename"): save console history to {output_filename}.py')
        print('self.load("input_filename"): load and run {input_filename}.py')
        print('self.goto_block(block_number): Change context to a past block number')

    def where(self):
        print(f'You are {len(self.blocks)} blocks deep.')
        print(f'The block journey is {self.blocks}')

    def save(self, filename):
        ipython = IPython.get_ipython()
        if ipython is not None:
            ipython.magic(f"%save {filename}.py")

    def load(self, filename):
        ipython = IPython.get_ipython()
        if ipython is not None:
            ipython.magic(f"%load {filename}.py")

    def goto_block(self, to_block: int):
        """
        Change context to a new block number.
        """
        self.context.run_model(self.slug, block_number=to_block)

    def _model_manifests(self, fetch_deployed):
        if len(self._model_manifest_map) == 0:
            loader: ModelLoader = self.context.model_loader  # type: ignore
            manifests = loader.loaded_model_manifests()
            for m in manifests:
                # hack for casing.
                m['displayName'] = m['display_name']
                self._model_manifest_map[m['slug']] = m

        if fetch_deployed and not self._added_deployed_manifests:
            model_api: ModelApi = self.context.model_api  # type: ignore
            try:
                deployed_manifests = model_api.get_models()
                for m in deployed_manifests:
                    self._model_manifest_map[m['slug']] = m
                self._added_deployed_manifests = True
            except Exception:
                # Error will have been logged but we continue so things work offline
                pass
        return self._model_manifest_map

    def list_models(self):
        manifest_map = self._model_manifests(True)
        slugs = list(manifest_map.keys())
        slugs.sort()
        for s in slugs:
            print(f' - {s} : {manifest_map[s].get("displayName")}')

    def describe_model(self, slug: str):  # pylint: disable=arguments-differ
        manifest_map = self._model_manifests(False)
        manifest = manifest_map.get(slug)
        if manifest is None:
            manifest_map = self._model_manifests(True)
            manifest = manifest_map.get(slug)
        print('')
        if manifest is not None:
            print_manifest_description(manifest, sys.stdout)
        else:
            print(f'No models matching "{slug}" found.')

    def run(self, _) -> dict:
        self.blocks.append(self.context.block_number)

        list_models = self.list_models
        describe_model = self.describe_model
        ledger = self.context.ledger
        run_model = self.context.run_model
        models = self.context.models
        block_number = self.context.block_number
        chain_id = self.context.chain_id
        web3 = self.context.web3
        run_model_historical = self.context.historical.run_model_historical
        run_model_historical_blocks = self.context.historical.run_model_historical_blocks

        if len(self.blocks) == 1:
            banner1 = f'Entering Credmark Model Console at block {self.context.block_number}.'
            banner2 = 'Help: self.help(), Quit: quit()\n' \
                'Available types are BlockNumber, Address, Contract, Token...\n'
            exit_msg = f'\nExiting Credmark Model Console at block {self.context.block_number}. '
        else:
            banner1 = f'\nSwitching context to block {self.context.block_number}.'
            banner2 = 'Quit current context: quit()\n'
            exit_msg = (f'\nExiting context at block {self.context.block_number}. '
                        f'\nCurrent context at block {self.blocks[-2]}. '
                        f'Remaining block stack {self.blocks[:-2]}.')

        IPython.embed(banner1=banner1,
                      banner2=banner2,
                      exit_msg=exit_msg)

        self.blocks.pop()
        return {'block_number': self.context.block_number}
