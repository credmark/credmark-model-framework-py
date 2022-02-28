from pydantic import Json
from credmark.types import DTO, Json
from credmark.types.data import Contract, Address


class ContractUtil:

    def __init__(self,
                 context,
                 ) -> None:
        self.context = context

    def load_description(self,
                         address: str = None,
                         name: str = None,
                         protocol: str = None,
                         product: str = None,
                         abi: dict = None,
                         tags: dict = None,):
        if name is None and address is None and abi is None:
            raise Exception

            # This means we can end up with different KINDS of contracts together. probably no bueno
            # we could do it if we could return a contract that is a subclass of web3.contract.Contract
            # but I don't understand how to do that with a web3 context

        contracts = []
        q = {}

        if address is not None:
            q["contractAddress"] = address
        if name is not None:
            q["contractName"] = name
        if protocol is not None:
            q["protocol"] = protocol
        if product is not None:
            q["product"] = product
        if tags is not None:
            q["tags"] = tags
        if abi is not None:
            q["abi"] = abi

        contract_q_results = self.context.run_model('contract.metadata', q)
        for contract in contract_q_results['contracts']:
            print(contract)
            contracts.append(Contract(context=self.context, **contract))
        return contracts

    def load_address(self, address: str):
        contract_q_results = self.context.run_model(
            'contract.metadata', {'contractAddress': address})
        contract_obj = Contract(context=self.context, **(contract_q_results['contracts'][0]))

        return contract_obj
