from abc import abstractmethod
import webbrowser
from typing import Any, Dict, List
import tempfile
import zipfile
import sys
import os
import importlib


from typing import (
    Dict,
    Tuple,
    Any,
    List,
    Callable,
    TypedDict,
    Optional,
    Union,
    Generator,
    Iterator,
)

from web3 import HTTPProvider, Web3

import dask.distributed as dask_dist

from dask.optimization import (
    cull,
    inline,
    inline_functions,
    fuse,
)
from credmark.model.errors import ModelRunError

from credmark.types.data.address import Address

import credmark
import types
import networkx as nx


def reload_models(mod):
    mod = importlib.reload(mod)
    reloaded = []
    for k, v in mod.__dict__.items():
        if isinstance(v, types.ModuleType):
            setattr(mod, k, importlib.import_module(v.__name__))
            reloaded.append((k, v))
    return reloaded


class ClusterResult(TypedDict):
    result: Dict[str, Any]
    dsk: Union[dict, nx.DiGraph]
    deps: Dict[str, str]
    futures: List[Any]


class SeqClient:
    client: str = 'sequence'

    def run_graph(self, dag: nx.DiGraph, outputs: List[Any]) -> ClusterResult:
        dag_reversed = dag.reverse()

        pruned_ts = []
        for node_out in outputs:
            # prune
            t1 = nx.dfs_tree(dag_reversed, source=node_out).reverse()
            pruned_ts.append(t1)

        if len(pruned_ts) > 1:
            pruned_t = nx.compose(*pruned_ts)
        else:
            pruned_t = pruned_ts[0]

        sorted_nodes = nx.algorithms.topological_sort(pruned_t)
        res_dict = {}
        dep_nodes = {}
        for node_exec in list(sorted_nodes):
            es = nx.edges(dag_reversed, [node_exec])
            if es is not None:
                node_deps = [d[1] for d in es]
            else:
                node_deps = []
            dep_nodes[node_exec] = dep_nodes.get(node_exec, []).extend(node_deps)
            dep_ress = {}
            for n_dep in node_deps:
                dep_ress[n_dep] = res_dict[n_dep]

            call_params = dag.nodes[node_exec]['call']
            call_func = call_params[0]
            call_args = list(call_params[1:])
            call_n_skip = call_args[1]
            for n_dep, dep_res in dep_ress.items():
                call_args[call_args.index(n_dep)] = dep_res

            res_dict[node_exec] = call_func(*call_args, *[() for _ in range(call_n_skip)])

        return ClusterResult(result={'result': res_dict},
                             dsk=dag,
                             deps=dep_nodes,
                             futures=[])


class DaskClient:
    def __init__(self, web3_http_provider, block_number, cluster_str, model_paths, open_browser):
        self.web3_http_provider = web3_http_provider
        self.block_number = block_number

        threads_per_worker = 1
        if cluster_str.startswith('tcp://'):
            client = dask_dist.Client(address=cluster_str, set_as_default=False,)
            print(
                f'Connected to cluster at {cluster_str} with dashboard at {client.dashboard_link}')
            self.__client = client
            self.upload_mods(model_paths)
        elif cluster_str.startswith('localhost:'):
            n_workers = int(cluster_str[cluster_str.index(':') + 1:])
            client = dask_dist.Client(
                n_workers=n_workers, threads_per_worker=threads_per_worker, set_as_default=False,)
            print(f'Launched local cluster with dashboard at {client.dashboard_link}')
            self.__client = client
        else:
            raise ModelRunError(f'Invalid cluster setup config = {cluster_str}')

        if open_browser:
            dashboard_link = client.dashboard_link
            if dashboard_link:
                webbrowser.open(dashboard_link, new=1)

    def upload_mods(self, mod_paths):
        def everything(s):
            # print(s)
            return True

        fp = tempfile.NamedTemporaryFile('w', suffix='.zip', prefix='models_pkg_')
        fp.close()

        with zipfile.PyZipFile(fp.name, mode="w", optimize=2) as zip_pkg:
            for mod_dir in mod_paths:
                all_init_files = []
                fp_init = os.path.join(mod_dir, '__init__.py')
                if not os.path.isfile(fp_init):
                    with open(fp_init, 'w') as f:
                        f.write('')
                        all_init_files.append(fp_init)
                for root, dirs, _files in os.walk(mod_dir):
                    for name in dirs:
                        if name != '__pycache__':
                            fp_init = os.path.join(root, name, '__init__.py')
                            if not os.path.isfile(fp_init):
                                with open(fp_init, 'w') as f:
                                    f.write('')
                                    all_init_files.append(fp_init)

                zip_pkg.writepy(mod_dir, filterfunc=everything)

        self.__client.upload_file(fp.name)
        self.__client.submit(lambda x: sys.path, 0).result()
        for mod_dir in mod_paths:
            mod = importlib.import_module(mod_dir)
            self.__client.submit(lambda x, mod=mod: reload_models(mod), 1).result()
        os.remove(fp.name)

    def run_graph(self, dsk: Dict[str, Tuple], outputs: List[Any], inline_funcs: List[Callable] = [], clear=True) -> ClusterResult:
        assert type(dsk) == dict
        assert type(outputs) == list

        try:
            dsk_opt1, dsk_deps1 = cull(dsk, keys=outputs)
        except KeyError as e:
            raise ValueError(f'[cull] Found undefined output {e} in the graph {dsk}')

        try:
            dsk_opt2 = inline(dsk_opt1, keys=outputs, dependencies=dsk_deps1)
        except Exception as e:
            raise ValueError(f'[inline]: {e}')

        if len(inline_funcs) == 0:
            try:
                dsk_opt3 = inline_functions(dsk_opt2, output=outputs, fast_functions=inline_funcs,  # [len, str.split]
                                            dependencies=dsk_deps1)
            except Exception as e:
                raise ValueError(f'[inline_functions]: {e}')
        else:
            dsk_opt3 = dsk_opt2

        try:
            dsk_opt4, dsk_deps4 = fuse(dsk_opt3, keys=outputs, dependencies=dsk_deps1)
        except Exception as err:
            raise ValueError(f'[fuse]: {err}')

        res_dict = {}
        dsk_deps4 = dsk_deps1
        try:
            res_future: Generator[dask_dist.Future, None, None] = self.__client.get(
                dsk_opt4, outputs, sync=False)
            res_dict = {k: v.result() for k, v in zip(outputs, res_future)}
        except Exception as err:
            raise err
        finally:
            if clear:
                # client can cache results with the same name. Use cancel to clear the calculations.
                # [ v.cancel() for k, v in zip(outputs, res_future)]
                return ClusterResult(result=res_dict,
                                     dsk=dsk_opt4,
                                     deps=dsk_deps4,
                                     futures=[])
            else:
                return ClusterResult(result=res_dict,
                                     dsk=dsk_opt4,
                                     deps=dsk_deps4,
                                     futures=res_future)

    def init_web3(self, force=False):
        worker = dask_dist.get_worker()
        http_provider = self.web3_http_provider
        block_number = self.block_number
        with worker._lock:
            if not hasattr(worker, "_web3"):
                setattr(worker, '_web3', {})
                has_web3 = False
            else:
                web3 = getattr(worker, '_web3')
                has_web3 = (http_provider in web3 and
                            block_number in web3[http_provider] and
                            not force)
            if not has_web3:
                web3 = Web3(HTTPProvider(http_provider))
                web3.eth.default_block = block_number if \
                    block_number is not None else 'latest'
                setattr(worker, '_web3', {http_provider: {block_number: {'web3': web3}}})
                return True
            else:
                return False

    def get_contract(self, contract_address: Address, contract_abi: str):
        worker: dask_dist.Worker = dask_dist.get_worker()
        self.init_web3()
        self.create_contract(contract_address, contract_abi)
        http_provider = self.web3_http_provider
        block_number = self.block_number
        with worker._lock:
            contract = getattr(worker, '_web3')[http_provider][block_number][contract_address]
            return contract

    def get_contract_function(self, contract_address: Address, contract_abi: str, func_name: str):
        worker: dask_dist.Worker = dask_dist.get_worker()
        contract = self.get_contract(contract_address, contract_abi)
        with worker._lock:
            func = contract[func_name]
            return func

    def contract_function_call(self, contract_address: Address, contract_abi: str, func_name: str, *param):
        worker = dask_dist.get_worker()
        contract_func = self.get_contract_function(contract_address, contract_abi, func_name)
        with worker._lock:
            result = contract_func(*param).call()
            return result

    def clear_all(self):
        # clean all futures
        who_has: dask_dist.WhoHas = self.__client.who_has()
        for k in who_has.keys():
            dask_dist.Future(k, client=self.__client).cancel()


class CreateContract(dask_dist.Worker):
    def __new__(cls, *a, **b):
        return dask_dist.Worker.__new__(cls)

    def __call__(self, web3_http_provider, block_number, contract_address: Address, contract_abi: str, force=False):
        with self._lock:
            web3_dict = getattr(self, '_web3')[web3_http_provider][block_number]
            web3 = web3_dict['web3']
            if contract_address not in web3_dict or force:
                contract = web3.eth.contract(
                    address=contract_address.checksum,
                    abi=contract_abi)
                web3_dict[contract_address] = contract
                return True
            else:
                return False


class Cluster():
    """
    A class provides launch and/or connect to a Dask Host.
    """

    def __init__(self,
                 web3_http_provider: str,
                 block_number: int,
                 cluster_str: str,
                 model_paths: List[str],
                 open_browser=False
                 ):
        threads_per_worker = 1
        if cluster_str == 'sequence':
            client = SeqClient()
            print('Use sequence cluster')
            dashboard_link = None
        else:
            client = DaskClient(web3_http_provider, block_number,
                                cluster_str, model_paths, open_browser)
        self.__client = client

    @ property
    def client(self):
        return self.__client
