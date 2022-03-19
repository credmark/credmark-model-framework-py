
from typing import List
from credmark.dto import DTO, DTOField, IterableListGenericDTO, PrivateAttr


class RpcBlockStartEndIntervalInput(DTO):
    start: int
    end: int
    interval: int


class RpcBlockWindowIntervalInput(DTO):
    window: int
    interval: int


class RpcBlockNumber(DTO):
    blockNumber: int
    blockTimestamp: int
    sampleTimestamp: int


class RpcBlockRangeOutput(IterableListGenericDTO[RpcBlockNumber]):
    blockNumbers: List[RpcBlockNumber] = DTOField(default=[], description='List of block numbers')
    _iterator: str = PrivateAttr('blockNumbers')
