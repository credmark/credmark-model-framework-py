from typing import List
from credmark.types import DTO, DTOField


class SeriesBlockOutput(DTO):
    blockNumber: int = DTOField(..., description='Block number in the series')
    output: dict = DTOField(..., description='Output of the model run for this block')


class SeriesModelOutput(DTO):
    """
    A DTO for the output of "series.*" models which run another
    model over a series of blocks.

    The output dict for a SeriesBlockOutput can be converted to
    a DTO by calling model.convert_dict_to_dto(). For example
    from within a model:

        obj: AModelDto = self.convert_dict_to_dto(output.series[0].output, AModelDto)
    """
    series: List[SeriesBlockOutput] = DTOField([], description='List of series block outputs')
