from eth_typing.evm import ChecksumAddress


class ContractUtil:

    def __init__(self,
                 context,
                 ) -> None:
        self.context = context

    def load(self,
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
            contracts.append(self.context.web3.eth.contract(
                address=self.context.web3.toChecksumAddress(contract['address']),
                abi=contract['abi']
            ))

        return contracts
