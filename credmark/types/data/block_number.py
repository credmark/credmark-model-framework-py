from typing import Union
from datetime import datetime
from web3.types import BlockData, Timestamp
from credmark.dto import DTO
import credmark.model
from credmark.model.errors import (ModelErrorDTO,
                                   ModelInvalidStateError,
                                   ModelNoContextError,
                                   ModelRunError)


class BlockNumberOutOfRangeDetailDTO(DTO):
    blockNumber: Union[int, None]
    maxBlockNumber: Union[int, None]


class BlockNumberOutOfRangeErrorDTO(ModelErrorDTO[BlockNumberOutOfRangeDetailDTO]):
    """
    A block number was constructed that is out of range for the context.
    This is a subclass of ModelInvalidStateError (and ModelRunError)
    as its considered a coding error in the model.

    Properties of the detail object:
    - blockNumber: the requested block number
    - maxBlockNumber: Maximum block number of context
    """


class BlockNumberOutOfRangeError(ModelInvalidStateError):
    dto_class = BlockNumberOutOfRangeErrorDTO

    @classmethod
    def create(cls, block_number: int, max_block_number: int):
        message = f'BlockNumber {block_number} is out of maximum range: {max_block_number}'
        detail = BlockNumberOutOfRangeDetailDTO(
            blockNumber=block_number, maxBlockNumber=max_block_number)
        return BlockNumberOutOfRangeError(message=message, detail=detail)


class InvalidBlockNumberError(ModelRunError):

    @classmethod
    def create(cls):
        return InvalidBlockNumberError(
            message='BlockNumber constructed with no number or sample_timestamp')


class BlockNumber(int):
    def __new__(cls,
                number: Union[int, None] = None,
                timestamp: Union[Timestamp, None] = None,  # pylint: disable=unused-argument
                sample_timestamp: Union[Timestamp, None] = None):
        context = credmark.model.ModelContext.current_context

        if number is None:
            if sample_timestamp is not None:
                if context is not None:
                    get_blocknumber_result = context.run_model(
                        'rpc.get-blocknumber', {"timestamp": sample_timestamp})
                    return BlockNumber(number=get_blocknumber_result['blockNumber'],
                                       timestamp=get_blocknumber_result['blockTimestamp'],
                                       sample_timestamp=sample_timestamp)
                else:
                    raise ModelNoContextError('No context to return a blockNumber for timestamp')
            else:
                raise InvalidBlockNumberError.create()
        if context is not None:
            max_block_number = context.block_number
        else:
            max_block_number = None

        if max_block_number is not None and number > max_block_number:
            raise BlockNumberOutOfRangeError.create(number, max_block_number)
        return super().__new__(BlockNumber, number)

    def __init__(self,
                 number: Union[int, None] = None,  # pylint: disable=unused-argument
                 timestamp: Union[Timestamp, None] = None,
                 sample_timestamp: Union[Timestamp, None] = None) -> None:
        self._timestamp = timestamp
        self.sample_timestamp = sample_timestamp
        super().__init__()

    def __add__(self, number):
        return BlockNumber(super().__add__(number))

    def __sub__(self, number):
        return BlockNumber(super().__sub__(number))

    def __timestamp__(self) -> Timestamp:
        if self._timestamp is None:
            context = credmark.model.ModelContext.current_context
            if context is not None:
                block: BlockData = context.web3.eth.get_block(self.__int__())
                if 'timestamp' in block:
                    self._timestamp = block['timestamp']
                    return self._timestamp
            raise ModelNoContextError('No _timestamp/context to return a timestamp')
        else:
            return self._timestamp

    def to_datetime(self):
        return datetime.fromtimestamp(self.__timestamp__())

    @ property
    def timestamp(self) -> Timestamp:
        return self.__timestamp__()

    @ property
    def datestring(self) -> str:
        return str(self.to_datetime())

    # TODO: Add checking that we aren't looking into the future
    # TODO: Add BlockRange type
