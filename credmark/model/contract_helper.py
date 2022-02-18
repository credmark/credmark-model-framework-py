from typing import Optional
from eth_typing.evm import ChecksumAddress


class ContractHelper:

    def __init__(self,
                 context,
                 ) -> None:
        self.context = context

    def get_contracts(self,
                      address: str = None,
                      name: str = None,
                      protocol: str = None,
                      product: str = None,
                      abi: dict = None,
                      ):
        if address is not None:
            contract = self.context.run_model('contract.metadata', {"contractAddress": address})
        if name is not None:

            conts = self.context.run_model('contract.metadata', {"contractName": name})
            contracts = []
            for cont in conts:
                contracts.append(self.context.web3.eth.contract(
                    address=self.context.web3.toChecksumAddress(cont['ADDRESS']),
                    abi=cont['ABI']
                ))
            return contracts
