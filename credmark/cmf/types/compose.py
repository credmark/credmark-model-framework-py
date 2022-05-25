from typing import Any, Union, List
from credmark.dto import DTO, DTOField, PrivateAttr, IterableListGenericDTO
from datetime import datetime
import pytz


class ModelDefinitionDto(DTO):
    slug: str = DTOField(default=None, description="The model version to execute.")
    version: Union[str, None] = DTOField(default=None, description="The model version to execute.")


class ComposeEachInputDto(DTO):
    destination: ModelDefinitionDto = DTOField(description="The model to be run on each input.")
    input: List = DTOField(description="The list of inputs to be iterated on.")


class ComposeEachOutputDto(IterableListGenericDTO):
    class ComposeEachOutputRowDto(DTO):
        input: Union[dict, DTO]
        output: Union[dict, DTO]
    destination: ModelDefinitionDto
    outputs: List[ComposeEachOutputRowDto]
    _iterator: str = PrivateAttr('outputs')


class ComposeHistoricalInputDto(DTO):
    destination: ModelDefinitionDto = DTOField(description="The model to be run historically.")
    input: dict = DTOField(description="The model input.")
    window: str = DTOField(description="The width of the historical window, e.g. '365 days'")
    interval: str = DTOField(description="The size of the sampling interval, e.g. '6 hours'")
    tz_offset: int = DTOField(default=0,
                              description="The timezone offset")
