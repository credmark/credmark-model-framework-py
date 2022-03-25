from typing import (
    Union
)
import logging
from datetime import (
    datetime,
    timezone,
)
from web3.types import (
    BlockData,
    Timestamp,
)

from credmark.dto import (
    DTO
)

import credmark.model
from credmark.model.errors import (ModelErrorDTO,
                                   ModelInvalidStateError,
                                   ModelNoContextError)


logger = logging.getLogger(__name__)


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


class BlockNumber(int):
    def __new__(cls,
                number: int,
                timestamp: Union[Timestamp, None] = None,  # pylint: disable=unused-argument
                sample_timestamp: Union[Timestamp, None] = None):  # pylint: disable=unused-argument
        context = credmark.model.ModelContext.current_context
        if context is not None:
            if number > context.block_number:
                raise BlockNumberOutOfRangeError.create(number, context.block_number)
        return super().__new__(BlockNumber, number)

    def __init__(self,
                 number: int,  # pylint: disable=unused-argument
                 timestamp: Union[Timestamp, None] = None,
                 sample_timestamp: Union[Timestamp, None] = None) -> None:
        self._timestamp = timestamp
        self.sample_timestamp = sample_timestamp
        super().__init__()

    def __add__(self, number):
        return BlockNumber(super().__add__(number))

    def __sub__(self, number):
        return BlockNumber(super().__sub__(number))

    @property
    def timestamp(self) -> Timestamp:
        if self._timestamp is None:
            context = credmark.model.ModelContext.current_context
            if context is None:
                raise ModelNoContextError('No _timestamp/context to return a timestamp')

            block: BlockData = context.web3.eth.get_block(self.__int__())
            if 'timestamp' in block:
                self._timestamp = block['timestamp']
                return self._timestamp

        return self._timestamp

    def to_datetime(self) -> datetime:
        return datetime.fromtimestamp(self.timestamp, tz=timezone.utc)

    @property
    def datestring(self) -> str:
        return str(self.to_datetime())

    @classmethod
    def from_timestamp(cls, timestamp: int):
        """
        Returns the BlockNumber from the input timestamp.
        """
        context = credmark.model.ModelContext.current_context
        if context is None:
            raise ModelNoContextError('No current context for BlockNumber.from_timestamp()')

        get_blocknumber_result = context.models.rpc.get_blocknumber(input=dict(timestamp=timestamp))
        if get_blocknumber_result['blockNumber'] > context.block_number:
            raise BlockNumberOutOfRangeError.create(
                get_blocknumber_result['blockNumber'], context.block_number)

        return BlockNumber(number=get_blocknumber_result['blockNumber'],
                           timestamp=get_blocknumber_result['blockTimestamp'],
                           sample_timestamp=get_blocknumber_result['sampleTimestamp'])
