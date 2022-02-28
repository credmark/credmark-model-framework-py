from pydantic import (  # pylint: disable=locally-disabled, unused-import
    BaseModel as DTO,
    Field as DTOField,
    constr,
    validator,
    Json as DTOJson,
    Extra as DTOExtra,
    PrivateAttr,
)

def fixstr(fixed_length):
    return constr(min_length=fixed_length, max_length=fixed_length)