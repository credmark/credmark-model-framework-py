from typing import (
    Dict,
    Any,
)

import json

from credmark.types import DTO, Json


class JsonStr(str):
    class JsonDTO(DTO):
        json_str: Json

    @ classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None:
        field_schema.update(type='string', format='json-string')

    @ classmethod
    def __get_validators__(cls):
        yield cls.validate

    @ classmethod
    def validate(cls, json_str: str) -> str:
        cls.JsonDTO(json_str=json_str)
        return json_str


class JsonDict(dict):
    class JsonDTO(DTO):
        json_dict: Json

    @ classmethod
    def __modify_schema__(cls, field_schema: Dict[dict, Any]) -> None:
        field_schema.update(type='dict', format='json-dict')

    @ classmethod
    def __get_validators__(cls):
        yield cls.validate

    @ classmethod
    def validate(cls, json_dict: dict) -> str:
        cls.JsonDTO(json_dict=json.dumps(json_dict))
        return json_dict


class JsonList(list):
    class JsonDTO(DTO):
        json_list: Json

    @ classmethod
    def __modify_schema__(cls, field_schema: Dict[list, Any]) -> None:
        field_schema.update(type='dict', format='json-list')

    @ classmethod
    def __get_validators__(cls):
        yield cls.validate

    @ classmethod
    def validate(cls, json_list: dict) -> list:
        cls.JsonDTO(json_list=json.dumps(json_list))
        return json_list
