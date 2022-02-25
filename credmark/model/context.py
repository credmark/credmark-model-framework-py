from abc import abstractmethod
from typing import Any, Type, TypeVar, Union, overload

from .errors import ModelRunError
from .ledger import Ledger
from .web3 import Web3Registry


from credmark.types import DTO
from credmark.types.data.block_number import BlockNumber
from credmark.utils.contract_util import ContractUtil

DTOT = TypeVar('DTOT')


class ModelContext():

    """
    Base model context class

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
        self.block_number = BlockNumber(block_number, self)
        self._web3 = None
        self._web3_registry = web3_registry
        self._ledger = None
        self._contract_util = None

    @property
    def web3(self):
        if self._web3 is None:
            self._web3 = self._web3_registry.web3_for_chain_id(self.chain_id)
            self._web3.eth.default_block = self.block_number if \
                self.block_number is not None else 'latest'
        return self._web3

    @property
    def ledger(self):
        if self._ledger is None:
            self._ledger = Ledger(self)
        return self._ledger

    @property
    def contracts(self):
        if self._contract_util is None:
            self._contract_util = ContractUtil(self)
        return self._contract_util

    @overload
    @abstractmethod
    def run_model(self,
                  slug: str,
                  input: Union[dict, DTO, None],
                  return_type: Type[DTOT],
                  block_number: Union[int, None] = None,
                  version: Union[str, None] = None,
                  ) -> DTOT: ...

    @overload
    @abstractmethod
    def run_model(self,
                  slug: str,
                  input: Union[dict, DTO, None] = None,
                  return_type: Union[Type[dict], None] = None,
                  block_number: Union[int, None] = None,
                  version: Union[str, None] = None,
                  ) -> dict: ...

    @abstractmethod
    def run_model(self,
                  slug,
                  input=None,
                  return_type=None,
                  block_number=None,
                  version=None,
                  ) -> Any:
        """Run a model by slug and optional version.

        Parameters:
            slug (str): the slug of the model
            input (dict | None): an optional dictionary of
                  input data that will be passed to the model when it is run.
            block_number (int | None): optional block number to use as context.
                  If None, the block_number of the current context will be used.
            version (str | None): optional version of the model.
                  If version is None, the latest version of
                  the model is used.
            return_type (DTO Type | None): optional class to use for the
                  returned output data. If not specified, returned value is a dict.
                  If a DTO specified, the returned value will be an instance
                  of that class if the output data is compatible with it. If its not,
                  an exception will be raised.

        Returns:
            The output returned by the model's run() method as a dict
            or a DTO instance if return_type is specified.

        Raises:
            MissingModelError if requested model is not available
            Exception on other errors
        """

    def transform_data_for_dto(self,
                               data: Union[dict, DTO, None],
                               dto: Union[Type[DTO], None],
                               slug: str,
                               data_source: str):
        try:
            if dto is None:
                if data is None:
                    return {}
                if isinstance(data, dict):
                    return data
                else:
                    return data.dict()
            else:
                if data is None:
                    return dto
                if isinstance(data, dto):
                    return data
                if isinstance(data, dict):
                    return dto(**data)
                else:
                    return dto(**data.dict())
        except Exception as e:
            raise ModelRunError(
                f'Error validating model {slug} {data_source}: {e}, with data={data}')
