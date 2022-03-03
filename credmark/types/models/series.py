from typing import List, Union
from credmark.types.dto import DTO, DTOField


class BlockSeriesRowDTO(DTO):
    blockNumber: int = DTOField(..., description='Block number in the series')
    blockTimestamp: int = DTOField(..., description='The Timestamp of the Block')
    sampleTimestamp: int = DTOField(..., description='The Sample Blocktime')
    output: dict = DTOField(..., description='Output of the model run for this block')


class BlockSeriesDTO(DTO):
    """
    A DTO for the output of "series.*" models which run another
    model over a series of blocks.

    The output dict for a SeriesBlockOutput can be converted to
    a DTO by calling model.convert_dict_to_dto(). For example
    from within a model:

        obj: AModelDto = self.convert_dict_to_dto(output.series[0].output, AModelDto)
    """
    series: List[BlockSeriesRowDTO] = DTOField([], description='List of series block outputs')

    def get(self, block_number = None, timestamp = None):
        if block_number is not None:
            return next((x for x in self.series if x.blockNumber == block_number), None)
        if timestamp is not None:
            return self.get(max(s.blockNumber for s in [s for s in self.series if s.blockTimestamp <= timestamp]))

    def __getitem__(self, idx):
        return self.series[idx]

    def __call__(self, idx):
        return self.series[idx]
            

class SeriesModelInput(DTO):
    window: int = None
    interval: int
    start: int = None
    end: int = None
    modelInput: Union[dict, DTO]
    modelSlug: str
    modelVersion: str = None