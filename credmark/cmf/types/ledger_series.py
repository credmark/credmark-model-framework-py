from typing import List, Union

from credmark.dto import DTO, DTOField

from .block_number import BlockNumber


class LedgerBlockTimeSeriesInput(DTO):
    """
    Input for the ledger.block-time-series model.
    """
    endTimestamp: int = DTOField(
        description='End timestamp of block series, inclusive unless exclusive is True')
    interval: int = DTOField(description='Series interval in seconds')
    count: int = DTOField(description='Number of intervals in the series.')
    exclusive: Union[bool, None] = DTOField(
        default=False, description='If true, blocks are exclusive of end timestamp')


class LedgerBlockNumberTimeSeries(DTO):
    """
    Output for the ledger.block-time-series model.
    """
    endTimestamp: int = DTOField(
        description='End timestamp of block series, inclusive unless exclusive is True')
    interval: int = DTOField(description='Series interval in seconds')
    exclusive: Union[bool, None] = DTOField(
        default=False, description='If true, blocks are exclusive of end timestamp')
    blockNumbers: List[BlockNumber] = DTOField(
        default=[],
        description='List of block numbers'
    )
