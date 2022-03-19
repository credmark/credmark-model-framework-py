from typing import List, Optional, TypeVar, Union, Generic
from credmark.dto import DTO, GenericDTO, DTOField, PrivateAttr, IterableListGenericDTO

DTOCLS = TypeVar('DTOCLS')


class BlockSeriesRow(GenericDTO, Generic[DTOCLS]):
    """
    A data row in a block series.
    The generic type specifies the class to use as the output.

    For example: row = BlockSeriesRow[MyOutputClass](**data)
    where row.output will be an instance of MyOutputClass
    """
    blockNumber: int = DTOField(..., description='Block number in the series')
    blockTimestamp: int = DTOField(..., description='The Timestamp of the Block')
    sampleTimestamp: int = DTOField(..., description='The Sample Blocktime')
    output: DTOCLS = DTOField(..., description='Output of the model run for this block')


class BlockSeries(IterableListGenericDTO[BlockSeriesRow[DTOCLS]], Generic[DTOCLS]):
    """
    A DTO for the output of "series.*" models which run another
    model over a series of blocks.

    The generic type specifies the class to use as the output
    in the BlockSeriesRow.

    For example: blockSeries = BlockSeries[MyOutputClass](**data)
    where blockSeries.series[0].output will be an instance of MyOutputClass
    """
    series: List[BlockSeriesRow[DTOCLS]] = DTOField(
        default=[], description='List of series block outputs')
    _iterator: str = PrivateAttr('series')

    def get(self, block_number=None, timestamp=None) -> Union[BlockSeriesRow[DTOCLS], None]:
        if block_number is not None:
            return next((x for x in self.series if x.blockNumber == block_number), None)
        if timestamp is not None:
            return self.get(block_number=max(s.blockNumber for s in
                                             [s for s in self.series if s.blockTimestamp <= timestamp]))
        return None


class SeriesModelStartEndIntervalInput(DTO):
    interval: int
    start: int
    end: int
    modelInput: Union[dict, DTO, None] = None
    modelSlug: str
    modelVersion: Optional[str] = None


class SeriesModelWindowIntervalInput(DTO):
    window: int
    interval: int
    modelInput: Union[dict, DTO, None] = None
    modelSlug: str
    modelVersion: Optional[str] = None
