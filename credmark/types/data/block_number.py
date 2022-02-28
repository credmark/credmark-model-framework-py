from datetime import datetime

from web3.types import BlockData, Timestamp

from typing import (
    Union,
)

class BlockNumber(int):
    def __new__(cls,
                number: Union[int, None] = None,
                context = None,
                timestamp: Union[Timestamp, None] = None,  # pylint: disable=unused-argument
                sample_timestamp: Union[Timestamp, None] = None):
        if number is None:
            if sample_timestamp is not None:
                if context is not None:
                    get_blocknumber_result = context.run_model(
                        'rpc.get-blocknumber', {"timestamp": sample_timestamp})
                    return BlockNumber(number=get_blocknumber_result['blockNumber'],
                                       context=context,
                                       timestamp=get_blocknumber_result['blockTimestamp'],
                                       sample_timestamp=sample_timestamp)
        else:
            return super().__new__(BlockNumber, number)

    def __init__(self,
                 number: Union[int, None] = None,  # pylint: disable=unused-argument
                 context = None, #: Union[ModelContext, None] = None,
                 timestamp: Union[Timestamp, None] = None,
                 sample_timestamp: Union[Timestamp, None] = None) -> None:
        self.context = context
        self._timestamp = timestamp
        self.sample_timestamp = sample_timestamp
        super().__init__()

    def __add__(self, number):
        return BlockNumber(super().__add__(number), self.context)

    def __sub__(self, number):
        return BlockNumber(super().__sub__(number), self.context)

    def __timestamp__(self) -> Timestamp:
        if self._timestamp is None:
            if self.context is not None:
                block: BlockData = self.context.web3.eth.get_block(self.__int__())
                if 'timestamp' in block:
                    self._timestamp = block['timestamp']
                    return self._timestamp
            raise ValueError('No _timestamp/context to return a timestamp')
        else:
            return self._timestamp

    def to_datetime(self):
        return datetime.fromtimestamp(self.__timestamp__())

    @property
    def timestamp(self) -> Timestamp:
        return self.__timestamp__()

    @property
    def datestring(self) -> str:
        return str(self.to_datetime())

    # TODO: Add checking that we aren't looking into the future
    # TODO: Add BlockRange type
