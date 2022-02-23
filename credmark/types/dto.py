from pydantic import BaseModel as DTO, Field as DTOField, constr  # pylint: disable=unused-import

__all__ = ['DTO', 'DTOField', 'fix_str']


def fix_str(fixed_length):
    return constr(min_length=fixed_length, max_length=fixed_length)
