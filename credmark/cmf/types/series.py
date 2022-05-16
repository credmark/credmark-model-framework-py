from typing import List, Optional, TypeVar, Union, Generic, Tuple, Callable
from credmark.dto import DTO, GenericDTO, DTOField, PrivateAttr, IterableListGenericDTO
from credmark.cmf.model.errors import ModelErrorDTO
import pandas as pd
from datetime import datetime

DTOCLS = TypeVar('DTOCLS')


class BlockSeriesRow(GenericDTO, Generic[DTOCLS]):
    """
    A data row in a block series.
    The generic type specifies the class to use as the output.

    For example ``row = BlockSeriesRow[MyOutputClass](**data)``
    where ``row.output`` will be an instance of ``MyOutputClass``
    """
    blockNumber: int = DTOField(..., description='Block number in the series')
    blockTimestamp: int = DTOField(..., description='The Timestamp of the Block')
    sampleTimestamp: int = DTOField(..., description='The Sample Blocktime')
    output: DTOCLS = DTOField(..., description='Output of the model run for this block')


class BlockSeriesErrorRow(DTO):
    """
    An error row in a block series.
    """
    blockNumber: int = DTOField(..., description='Block number in the series')
    blockTimestamp: int = DTOField(..., description='The Timestamp of the Block')
    sampleTimestamp: int = DTOField(..., description='The Sample Blocktime')
    error: ModelErrorDTO = DTOField(..., description='Error DTO of the model run for this block')


class BlockSeries(IterableListGenericDTO[BlockSeriesRow[DTOCLS]], Generic[DTOCLS]):
    """
    A DTO for the output of "series.*" models which run another
    model over a series of blocks.

    The generic type specifies the class to use as the output
    in the ``BlockSeriesRow``.

    For example ``blockSeries = BlockSeries[MyOutputClass](**data)``
    where ``blockSeries.series[0].output`` will be an instance of ``MyOutputClass``

    If a permanent error occurs during a model run, the block and error
    will be added to the errors array.
    If a non-permament error occurs during a model run, the entire series
    will generate an error.
    """
    series: List[BlockSeriesRow[DTOCLS]] = DTOField(
        default=[], description='List of series block outputs')
    errors: Union[List[BlockSeriesErrorRow], None] = DTOField(
        default=None,
        description='If any permanent (deterministic) errors were returned from model runs, '
        'this array will contain blocks with errors')
    _iterator: str = PrivateAttr('series')

    def append_error(self, error_row: BlockSeriesErrorRow):
        if self.errors is None:
            self.errors = []
        self.errors.append(error_row)

    def get(self, block_number=None, timestamp=None) -> Union[BlockSeriesRow[DTOCLS], None]:
        if block_number is not None:
            return next((x for x in self.series if x.blockNumber == block_number), None)
        if timestamp is not None:
            return self.get(
                block_number=max(s.blockNumber for s in
                                 [s for s in self.series if s.blockTimestamp <= timestamp]))
        return None

    def to_list(self, fields: Optional[List[Callable]] = None) -> List[List]:
        """
        Parameters:
            fields (List[Callable] | None): List of lambda to extract certain field from output.
                Leave empty to extract the entire output.
        Extract tuples from series data
        """
        if fields is None:
            return [[p.blockNumber,
                    datetime.utcfromtimestamp(p.blockTimestamp),
                    p.output]
                    for p in self.series]
        else:
            return [([p.blockNumber,
                    datetime.utcfromtimestamp(p.blockTimestamp)] +
                    [f(p.output) for f in fields])
                    for p in self.series]

    def to_dataframe(self, fields: Optional[List[Tuple[str, Callable]]] = None) -> pd.DataFrame:
        """
        Parameters:
            fields (List[Tuple[str, Callable]] | None): List of field name and lambda to extract
                certain field from output. Leave empty to extract the entire output.
        Extract tuples from series data

        """
        series_in_list = self.to_list(fields=None if fields is None else [f for (_, f) in fields])
        if fields is None:
            return pd.DataFrame(series_in_list, columns=['blockNumber', 'blockTime', 'output'])
        else:
            return pd.DataFrame(series_in_list,
                                columns=['blockNumber', 'blockTime'] + [c for c, _ in fields])


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
