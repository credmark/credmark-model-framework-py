from typing import List, Optional, Type, TypeVar, Union
from credmark.model.transform import transform_data_for_dto
from credmark.types.dto import DTO, DTOField, PrivateAttr, IterableListDto

DTOCLS = TypeVar('DTOCLS')


class BlockSeriesRow(DTO):
    blockNumber: int = DTOField(..., description='Block number in the series')
    blockTimestamp: int = DTOField(..., description='The Timestamp of the Block')
    sampleTimestamp: int = DTOField(..., description='The Sample Blocktime')
    output: dict = DTOField(..., description='Output of the model run for this block')
    _output_dto: Union[DTO, None] = PrivateAttr(None)

    def output_dto(self, dto_class: Type[DTOCLS]) -> DTOCLS:
        """
        Convert the output dict to a DTO instance
        """
        if self._output_dto is None:
            self._output_dto = transform_data_for_dto(  # type:ignore
                self.output, dto_class, 'block-series', 'output')  # type:ignore
        return self._output_dto  # type:ignore


class BlockSeries(IterableListDto):
    """
    A DTO for the output of "series.*" models which run another
    model over a series of blocks.

    The output dict for a SeriesBlockOutput can be converted to
    a DTO by calling series_row.output_dto(DTOClass). For example
    from within a model:

        obj: AModelDto = output.series[0].output_dto(AModelDto)
    """
    series: List[BlockSeriesRow] = DTOField([], description='List of series block outputs')
    _iterator = PrivateAttr('series')

    def get(self, block_number=None, timestamp=None):
        if block_number is not None:
            return next((x for x in self.series if x.blockNumber == block_number), None)
        if timestamp is not None:
            return self.get(max(s.blockNumber for s in
                                [s for s in self.series if s.blockTimestamp <= timestamp]))


class SeriesModelInput(DTO):
    window: Optional[int] = None
    interval: int
    start: Optional[int] = None
    end: Optional[int] = None
    modelInput: Union[dict, DTO]
    modelSlug: str
    modelVersion: Optional[str] = None
