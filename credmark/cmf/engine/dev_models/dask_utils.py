from credmark.types import Contract, Address

from typing import (
    Union,
    List,
)

import dask.distributed as dask_dist

from web3 import Web3, HTTPProvider

from credmark.types.data.address import Address


class DaskUtils:
    def __init__(self,
                 context,
                 ) -> None:
        self.context = context

    @staticmethod
    def call(f, *args, **kwargs):
        return f(*args, **kwargs)

    @staticmethod
    def get_worker():
        worker = dask_dist.get_worker()  # The worker on which this task is running
        return worker.address

    @staticmethod
    def get_client():
        client = dask_dist.get_client()
        return client

    def init_web3(self, force=False):
        worker = dask_dist.get_worker()
        http_provider = self.context.web3_proivder_url
        block_number = self.context.block_number
        with worker._lock:
            if not hasattr(worker, "_web3"):
                worker._web3 = {}
                has_web3 = False
            else:
                has_web3 = (http_provider in worker._web3 and
                            block_number in worker._web3[http_provider] and
                            not force)
            if not has_web3:
                web3 = Web3(HTTPProvider(http_provider))
                web3.eth.default_block = block_number if \
                    block_number is not None else 'latest'
                worker._web3[http_provider] = {block_number: {'web3': web3}}
                return True
            else:
                return False

    # TODO: they shall create from ContractDTO instead of address/abi.
    def create_contract(self, contract_address: Address, contract_abi: str, force=False):
        worker = dask_dist.get_worker()
        http_provider = self.context.web3_proivder_url
        block_number = self.context.block_number
        with worker._lock:
            web3_dict = worker._web3[http_provider][block_number]
            web3 = web3_dict['web3']
            if contract_address not in web3_dict or force:
                contract = web3.eth.contract(
                    address=contract_address.checksum,
                    abi=contract_abi)
                worker._web3[http_provider][block_number][contract_address] = contract
                return True
            else:
                return False

    def get_contract(self, contract_address: Address, contract_abi: str):
        worker = dask_dist.get_worker()
        self.init_web3()
        self.create_contract(contract_address, contract_abi)
        http_provider = self.context.web3_proivder_url
        block_number = self.context.block_number
        with worker._lock:
            contract = worker._web3[http_provider][block_number][contract_address]
            return contract

    def get_contract_function(self, contract_address: Address, contract_abi: str, func_name: str):
        worker = dask_dist.get_worker()
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
