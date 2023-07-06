from datetime import datetime
from typing import Callable, Generic, List, Optional, Tuple, TypeVar, Union

import pandas as pd

from credmark.cmf.model.errors import ModelErrorDTO
from credmark.dto import DTO, DTOField, DTOType, GenericDTO, IterableListGenericDTO, PrivateAttr

DTOCLS = TypeVar('DTOCLS')

__all__ = ['BlockSeriesRow', 'BlockSeriesErrorRow', 'BlockSeries',
           'SeriesModelStartEndIntervalInput', 'SeriesModelWindowIntervalInput']


class BlockSeriesRow(GenericDTO, Generic[DTOCLS]):
    """
    A data row in a block series.
    The generic type specifies the class to use as the output.

    For example ``row = BlockSeriesRow[MyOutputClass](**data)``
    where ``row.output`` will be an instance of ``MyOutputClass``
    """
    blockNumber: int = DTOField(..., description='Block number in the series')
    blockTimestamp: int = DTOField(...,
                                   description='The Timestamp of the Block')
    sampleTimestamp: int = DTOField(..., description='The Sample Block time')
    output: DTOCLS = DTOField(...,
                              description='Output of the model run for this block')


class BlockSeriesErrorRow(DTO):
    """
    An error row in a block series.
    """
    blockNumber: int = DTOField(..., description='Block number in the series')
    blockTimestamp: int = DTOField(...,
                                   description='The Timestamp of the Block')
    sampleTimestamp: int = DTOField(..., description='The Sample Block time')
    error: ModelErrorDTO = DTOField(...,
                                    description='Error DTO of the model run for this block')


# pylint: disable=not-an-iterable
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
    If a non-permanent error occurs during a model run, the entire series
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
        series_in_list = self.to_list(fields=None if fields is None else [
                                      f for (_, f) in fields])
        if fields is None:
            return pd.DataFrame(data=series_in_list, columns=['blockNumber', 'blockTime', 'output'])
        else:
            return pd.DataFrame(
                data=series_in_list,
                columns=['blockNumber', 'blockTime'] + [c for c, _ in fields])


class SeriesModelStartEndIntervalInput(DTO):
    interval: int
    start: int
    end: int
    modelInput: Union[dict, DTOType, None] = None
    modelSlug: str
    modelVersion: Optional[str] = None

    class Config:
        schema_extra = {'skip_test': True}


class SeriesModelWindowIntervalInput(DTO):
    window: int
    interval: int
    modelInput: Union[dict, DTOType, None] = None
    modelSlug: str
    modelVersion: Optional[str] = None

    class Config:
        schema_extra = {
            'example': {"modelSlug": "token.balance",
                        "modelInput": {
                            "address": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
                            "account": "0x55FE002aefF02F77364de339a1292923A15844B8"
                        }, "window": 20000, "interval": 10000}
        }


class ImmutableOutput(DTO):
    firstResultBlockNumber: int
