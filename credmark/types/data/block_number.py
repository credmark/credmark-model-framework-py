from typing import (
    Union
)
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
                                   ModelNoContextError,
                                   ModelInputError)


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
        if context is not None and number > context.block_number:
            raise BlockNumberOutOfRangeError.create(number, context.block_number)

        if number < 0:
            raise BlockNumberOutOfRangeError(message=f'BlockNumber {number} is less than 0',
                                             detail=BlockNumberOutOfRangeDetailDTO(blockNumber=number, maxBlockNumber=context.block_number))

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
    def timestamp(self) -> int:
        if self._timestamp is None:
            context = credmark.model.ModelContext.current_context
            if context is None:
                raise ModelNoContextError(
                    "credmark.model.ModelContext.current_context cannot be None")

            block: BlockData = context.web3.eth.get_block(self.__int__())
            if 'timestamp' not in block:
                raise ModelInputError(f'No timestamp for block {self.__int__()}')
            self._timestamp = block['timestamp']

        return self._timestamp

    @property
    def timestamp_datetime(self) -> datetime:
        return datetime.fromtimestamp(self.timestamp, tz=timezone.utc)

    @classmethod
    def from_timestamp(cls, timestamp: Union[datetime, int, float]):
        """
        Returns the block number from the input timestamp.
        For input of timestamp and datetime, the last block before the datetime is returned.

        The timestamp here will be used as the sample_timestamp on the resulting BlockNumber.
        """

        context = credmark.model.ModelContext.current_context
        if context is None:
            raise ModelNoContextError("credmark.model.ModelContext.current_context cannot be None")

        if isinstance(timestamp, int):
            pass
        elif isinstance(timestamp, float):
            timestamp = int(timestamp)
        elif isinstance(timestamp, datetime):
            if not timestamp.tzinfo:
                raise ModelInputError(f'Input datetime {timestamp} has no tzinfo.')
            timestamp = int(timestamp.timestamp())
        else:
            raise ModelInputError(
                f'Invalid input for date/datetime/timestamp to query block_number {timestamp}')

        get_blocknumber_result = context.models.rpc.get_blocknumber(timestamp=timestamp)

        return BlockNumber(number=get_blocknumber_result['blockNumber'],
                           timestamp=get_blocknumber_result['blockTimestamp'],
                           sample_timestamp=get_blocknumber_result['sampleTimestamp'])
