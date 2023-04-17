# pylint: disable=locally-disabled, unused-import, unused-variable, unused-wildcard-import, wildcard-import, line-too-long, protected-access, too-many-branches

import importlib
import importlib.util
import os
import sys
import json
from typing import Dict, List, NamedTuple, Optional
from web3.middleware.geth_poa import geth_poa_middleware
from web3 import HTTPProvider, Web3

import requests
from credmark.cmf.engine.context import EngineModelContext
from credmark.cmf.engine.model_loader import ModelLoader
from credmark.cmf.engine.model_api import GATEWAY_API_URL
from credmark.cmf.types import Network
from credmark.cmf.types.network import CREDMARK_PUBLIC_PROVIDERS

from IPython.core.magic import (Magics, cell_magic, line_cell_magic,
                                line_magic, magics_class, needs_local_scope)
from IPython.lib.pretty import pprint, pretty

from dotenv import dotenv_values


class CmfInit(NamedTuple):
    """
    Cmf Initialization Parameters

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
    chain_to_provider_url: Dict[str, str] = {}
    api_url: Optional[str] = None
    use_local_models: Optional[str] = None  # None, '*', or '-', or 'model_to_be_run_locally'
    register_utility_global: bool = True


def load_module_items(namespace, module_name, selection: Optional[List[str]] = None):
    imp = importlib.import_module(module_name)
    for a in dir(sys.modules[module_name]):
        if not a.startswith("_"):
            if selection is None or a in selection:
                namespace[a] = getattr(imp, a)


def create_cmf(cmf_param):
    """
    create cmf
    """
    context, _model_loader = create_cmf_context(cmf_param)

    model_loaded = _model_loader.loaded_model_version_lists()
    for _k, cache_value in model_loaded.items():
        try:
            assert len(cache_value) == 1
        except AssertionError:
            print(_k)
            raise

    model_loaded = {k: v[0] for k, v in model_loaded.items()}

    return context, model_loaded


def create_cmf_context(cmf_param):
    models_spec = importlib.util.find_spec("models")
    if models_spec is not None and models_spec.submodule_search_locations is not None:
        models_path = [models_spec.submodule_search_locations[0]]
    else:
        models_path = []

    dotenv_param = {}
    for pth in models_path:
        dotenv_file = os.path.realpath(os.path.join(pth, '..', '.env'))
        if os.path.isfile(dotenv_file):
            dotenv_param = dotenv_values(dotenv_file)
            break

    if isinstance(dotenv_param, dict) and 'CREDMARK_WEB3_PROVIDERS' in dotenv_param:
        provider_from_dotenv = json.loads(dotenv_param['CREDMARK_WEB3_PROVIDERS'])  # type: ignore
    else:
        provider_from_dotenv = {}

    providers_json = os.environ.get('CREDMARK_WEB3_PROVIDERS', None)
    if providers_json is not None:
        provider_from_environment = json.loads(providers_json)
    else:
        provider_from_environment = {}

    cmf_param['chain_to_provider_url'] = \
        provider_from_dotenv \
        | provider_from_environment \
        | cmf_param.get('chain_to_provider_url', {})

    for k, v in CREDMARK_PUBLIC_PROVIDERS.items():
        if k not in cmf_param['chain_to_provider_url']:
            cmf_param['chain_to_provider_url'][k] = v

    param = {
        'chain_id': 1,
        'block_number': None,
        'model_loader_path': models_path,
        'use_local_models': None,
        'register_utility_global': False,
        'api_url': GATEWAY_API_URL,
    } | cmf_param

    cmf_init = CmfInit(**param)

    default_models_path = os.path.abspath(importlib.import_module('models').__path__[0])
    model_loader_path = [os.path.abspath(p) for p in cmf_init.model_loader_path]
    if default_models_path not in model_loader_path:
        model_loader_path.append(default_models_path)

    for p in model_loader_path:
        if not os.path.isdir(p):
            raise ValueError(f'{p} specified for model_loader_path is not a valid path')

    provider_url = cmf_init.chain_to_provider_url.get(str(cmf_init.chain_id), None)
    if provider_url is None:
        print(f'Warning: missing provider for chain_id={cmf_init.chain_id}')
    else:
        # Test provider
        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            provider_url, data=f'{{"jsonrpc":"2.0","method": "eth_blockNumber","params": [], "id":{cmf_init.chain_id}}}',
            headers=headers,
            timeout=60)
        if response.status_code in [200, 201]:
            res = response.json()
            if 'result' in res and int(res['result'], base=16) > 0:
                pass
            else:
                raise ValueError(
                    f'Provider URL {provider_url} does not respond properly for querying block number: {res}')
        else:
            raise ValueError(
                f'Provider URL {provider_url} for {cmf_init.chain_id} does not respond.')

    model_loader = ModelLoader(model_loader_path, None, True)
    context = EngineModelContext.create_context(chain_id=cmf_init.chain_id, block_number=cmf_init.block_number, model_loader=model_loader,
                                                chain_to_provider_url=cmf_init.chain_to_provider_url,
                                                api_url=cmf_init.api_url, run_id=None, console=True, use_local_models=cmf_init.use_local_models)

    if param['chain_to_provider_url'][str(param['chain_id'])].startswith('http'):
        context._web3 = Web3(HTTPProvider(context.web3.provider.endpoint_uri,  # type: ignore
                             request_kwargs={'timeout': 3600 * 10}))

        if param['chain_id'] in [Network.Rinkeby,
                                 Network.BSC,
                                 Network.Polygon,
                                 Network.Optimism,
                                 Network.Avalanche]:
            context._web3.middleware_onion.inject(geth_poa_middleware, layer=0)

        context._web3.eth.default_block = int(context.block_number)

    return context, model_loader


@magics_class
class CredmarkMagic(Magics):

    @needs_local_scope
    @line_magic
    def cmf(self, line, local_ns):
        # pylint: disable=too-many-branches, too-many-statements, too-many-locals
        if line == 'help':
            print('Example:')
            param = CmfInit()._asdict()
            print('%reload_ext credmark.cmf.ipython')
            print('param = ' + pretty(param))
            print("""context, model_loader = %cmf param
# or
%cmf param
context, model_loader = _""")
            print("""Other commands:
- %cmf param -v: verbose
- %cmf default_param: returns default parameters
Example: param = %cmf default_param
- %cmf default: setup with default parameters
Example: context, model_loader = %cmf default
- %cmf help: get help
- %cmf help_param: get help for parameters
""")
            return None

        if line == 'help_param':
            print('Doc:')
            print(CmfInit.__doc__)
            return None

        if self.shell is None:
            raise ValueError('Shell is None')

        if line == 'default_param':
            return CmfInit()._asdict()

        if line == 'default':
            cmf_param = CmfInit()._asdict()
            print('Using default to initialize Cmf')
            pprint(cmf_param)
        else:
            params = line.split(' ')
            cmf_param = local_ns.get(params[0], None)
            verbose = False
            if len(params) == 2 and params[1] == '-v':
                verbose = True
            if cmf_param is None:
                raise ValueError(
                    f'Undefined variable {line} for cmf initialization. Get help from %cmf help')
            if not isinstance(cmf_param, dict):
                raise ValueError(
                    f'Variable {line} needs to be a dictionary. Get help from %cmf help')
            if verbose:
                print('Cmf to be initialized with:')
                pprint(cmf_param)

        context, model_loader = create_cmf_context(cmf_param)
        var_namespace = local_ns
        load_module_items(var_namespace, 'credmark.cmf.model', ['Model'])
        load_module_items(var_namespace, 'credmark.cmf.model.errors',
                          ['ModelDataError', 'ModelRunError'])
        load_module_items(var_namespace, 'credmark.cmf.types')
        load_module_items(var_namespace, 'credmark.dto')
        load_module_items(var_namespace, 'credmark.cmf.engine.dev_models.console',
                          ['get_dt', 'get_block', 'log_output'])

        if cmf_param.get('register_utility_global', True):
            var_namespace['ledger'] = context.ledger
            var_namespace['run_model'] = context.run_model
            var_namespace['models'] = context.models
            var_namespace['block_number'] = context.block_number
            var_namespace['chain_id'] = context.chain_id
            var_namespace['web3'] = context.web3
            var_namespace['run_model_historical'] = context.historical.run_model_historical
            var_namespace['run_model_historical_blocks'] = context.historical.run_model_historical_blocks

        return context, model_loader


def load_ipython_extension(ipy_module):
    ipy_module.register_magics(CredmarkMagic)
