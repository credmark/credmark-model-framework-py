from typing import (
    Dict,
    Any,
)

import json

from credmark.types.dto import DTO, DTOJson


class JsonSerializableObject(str):
    class JsonDTO(DTO):
        json_str: DTOJson

    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None:
        field_schema.update(type='string', format='json-string')

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, json_obj) -> str:
        cls.JsonDTO(json_str=json.dumps(json_obj))
        return json_obj
