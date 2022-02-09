from abc import abstractmethod
from typing import Union
from credmark.model.ledger import Ledger
from credmark.model.web3 import Web3Registry


class ModelContext():
    """Base model context class

    Instance attributes:
        chain_id (int): chain ID, ex 1
        block_number (int): default block number
        web3 (Web3): a configured web3 instance for RPC calls

    Methods:
        run_model(...) - run the specified model and return the results
    """

    def __init__(self, chain_id: int, block_number: int,
                 web3_registry: Web3Registry):
        self.chain_id = chain_id
        self.block_number = block_number
        self._web3 = None
        self.__ledger = None
        self.__web3_registry = web3_registry

    @property
    def web3(self):
        if self._web3 is None:
            self._web3 = self.__web3_registry.web3_for_chain_id(self.chain_id)
            self._web3.eth.default_block = self.block_number if \
                self.block_number is not None else 'latest'
        return self._web3

    @property
    def ledger(self):
        if self.__ledger is None:
            self.__ledger = Ledger(self)
        return self.__ledger

    @abstractmethod
    def run_model(self, name: str, input: Union[dict, None] = None,
                  block_number: Union[int, None] = None, version: Union[str, None] = None) -> dict:
        """Run a model by name and optional version.

        Parameters:
            name (str): the name of the model
            input (dict | None): an optional dictionary of
                  input data that will be passed to the model when it is run.
            block_number (int | None): optional block number to use as context.
                  If None, the block_number of the current context will be used.
            version (str | None): optional version of the model.
                  If version is None, the latest version of
                  the model is used.

        Returns:
            The result returned by the model's run() method.

        Raises:
            MissingModelError if requested model is not available
            Exception on other errors
        """
        self.__web = None
