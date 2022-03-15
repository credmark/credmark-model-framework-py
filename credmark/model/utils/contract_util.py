from credmark.types import Contract, Address
import credmark.model

from typing import (
    Union,
    List,
)


class ContractUtil:

    def __init__(self,
                 context,
                 ) -> None:
        self.context: credmark.model.ModelContext = context

    def load_description(self,
                         address: Union[Address, None] = None,
                         contract_name: Union[str, None] = None,
                         protocol: Union[str, None] = None,
                         product: Union[str, None] = None,
                         abi: Union[dict, None] = None,
                         tags: Union[dict, None] = None) -> List[Contract]:
        if contract_name is None and address is None and abi is None:
            raise Exception

            # TODO: name needs to be contract_name to avoid confusion with name().call() which is on ERC20s

            # This means we can end up with different KINDS of contracts together.
            # probably no bueno
            # we could do it if we could return a contract that is a subclass of web3.contract.Contract
            # but I don't understand how to do that with a web3 context

        contracts: List[Contract] = []
        q = {}

        if address is not None:
            q["contractAddress"] = address
        if contract_name is not None:
            q["contractName"] = contract_name
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
            contracts.append(
                Contract(_instance=None,
                         address=contract.get('contract_address'),
                         **contract))
        return contracts

    def load_address(self, address: str) -> Contract:
        contract_q_results = self.context.run_model(
            'contract.metadata', {'contractAddress': address})
        contract_obj = Contract(_instance=None,
                                address=address,
                                **(contract_q_results['contracts'][0]))
        return contract_obj
