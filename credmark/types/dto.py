from pydantic import (  # pylint: disable=locally-disabled, unused-import
    BaseModel as DTOBaseModel,
    Field as DTOField,
    constr,
    validator,
)


def fix_str(fixed_length):
    return constr(min_length=fixed_length, max_length=fixed_length)


class DTO(DTOBaseModel):
    pass
