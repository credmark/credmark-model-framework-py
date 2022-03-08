from typing import List, Optional, Union
from credmark.model.transform import transform_data_for_dto
from credmark.types.dto import DTO, DTOField, PrivateAttr, IterableListDto


class BlockSeriesRow(DTO):
    blockNumber: int = DTOField(..., description='Block number in the series')
    blockTimestamp: int = DTOField(..., description='The Timestamp of the Block')
    sampleTimestamp: int = DTOField(..., description='The Sample Blocktime')
    output: dict = DTOField(..., description='Output of the model run for this block')

    def output_dto(self, dto_class):
        """
        Convert the output dict to a DTO instance
        """
        return transform_data_for_dto(self.output, dto_class, 'block-series', 'output')


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
