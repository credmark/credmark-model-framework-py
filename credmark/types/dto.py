# pylint: disable=locally-disabled, unused-import

from pydantic import (
    BaseModel as DTO,
    Field as DTOField,
    constr,
    confloat,
    conint,
    validator,
    Json as DTOJson,
    Extra as DTOExtra,
    PrivateAttr,
)

def fixstr(fixed_length):
    return constr(min_length=fixed_length, max_length=fixed_length)