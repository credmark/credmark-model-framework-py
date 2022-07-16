# pylint: disable=locally-disabled, unused-import, unused-variable, unused-wildcard-import, wildcard-import, line-too-long

import importlib
import os
import sys
from typing import Dict, List, NamedTuple, Optional

import IPython.core.magic as ipython
from credmark.cmf.engine.context import EngineModelContext
from credmark.cmf.engine.model_loader import ModelLoader


class CmfInit(NamedTuple):
    """
    Cmf Initilization Parameters

    :param chain_id: Chain id, default to 1
    :param block_number: (Optional) None or int
    :param model_loader_path: List of path to the models directories
    :param chain_to_provider_url: A dictionary mapping chain ID to node RPC URL, e.g. {'1': 'http://192.168.68.122:10444'}
    :param api_url: (Optional) None or URL to Credmark gateway
    :param use_local_models: None (top-level models run local), '*' (all model run locally), or '-' (all models run remotely), or a comma-separated list of models
    :param register_utility_global: True (register global variables for utilities like ledger, default) or False
    """

    chain_id: int = 1
    block_number: Optional[int] = None
    model_loader_path: List[str] = []
    chain_to_provider_url: Dict[str, str] = {'1': 'http://192.168.68.122:10444'}
    api_url: Optional[str] = None
    use_local_models: Optional[str] = None  # None, '*', or '-', or 'model_to_be_run_locally'
    register_utility_global: bool = True


def load_module_items(module_name, namespace, selection: Optional[List[str]] = None):
    imp = importlib.import_module(module_name)
    for a in dir(sys.modules[module_name]):
        if not a.startswith("_"):
            if selection is None or a in selection:
                namespace[a] = getattr(imp, a)


@ipython.magics_class
class CredmarkMagic(ipython.Magics):
    @ipython.line_magic
    def cmf(self, line):
        if self.shell is None:
            raise ValueError('Shell is None')

        if line == 'help':
            print(CmfInit.__doc__)
            print(CmfInit()._asdict())
            return None

        param_ext = self.shell.user_ns.get(line, None)
        if param_ext is None:
            raise ValueError(
                f'Undefined variable {line} for cmf initialization. Get help from %cmf help')
        if not isinstance(param_ext, dict):
            raise ValueError(
                f'Variable {line} needs to be a dictionary. Get help from %cmf help')

        cmf_init = CmfInit(**param_ext)
        for p in cmf_init.model_loader_path:
            if not os.path.isdir(p):
                raise ValueError(f'{p} specified for model_loader_path is not a valid path')

        model_loader = ModelLoader(cmf_init.model_loader_path, None, True)
        context = EngineModelContext.create_context(chain_id=cmf_init.chain_id, block_number=cmf_init.block_number, model_loader=model_loader,
                                                    chain_to_provider_url=cmf_init.chain_to_provider_url,
                                                    api_url=cmf_init.api_url, run_id=None, console=True, use_local_models=cmf_init.use_local_models)

        var_namespace = self.shell.user_ns
        load_module_items('credmark.cmf.types', var_namespace)
        load_module_items('credmark.dto', var_namespace)
        load_module_items('credmark.cmf.model', var_namespace, ['Model'])
        load_module_items('credmark.cmf.model.errors', var_namespace,
                          ['ModelDataError', 'ModelRunError'])

        if cmf_init.register_utility_global:
            var_namespace['ledger'] = context.ledger
            var_namespace['run_model'] = context.run_model
            var_namespace['models'] = context.models
            var_namespace['block_number'] = context.block_number
            var_namespace['chain_id'] = context.chain_id
            var_namespace['web3'] = context.web3
            var_namespace['run_model_historical'] = context.historical.run_model_historical
            var_namespace['run_model_historical_blocks'] = context.historical.run_model_historical_blocks

        return context


def load_ipython_extension(ipy_module):
    ipy_module.register_magics(CredmarkMagic())
