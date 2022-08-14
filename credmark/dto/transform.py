import json
from typing import Type, Union

from credmark.dto.encoder import json_dumps

from . import DTOType, DTOTypesTuple


class DataTransformError(Exception):
    pass


def transform_dto_to_dict(data: Union[dict, DTOType, None]):
    # We use json_dumps to ensure any DTOs embedded in a dict
    # are serialized properly. If we just set the input in the
    # req object and let requests serializes, any embedded DTOs
    # would fail.
    input_json = json_dumps(data) if data is not None else '{}'
    input_json = json.loads(input_json)
    return input_json


def transform_data_for_dto(  # pylint: disable=too-many-return-statements
        data: Union[dict, DTOType, None],
        dto_class: Union[Type[DTOType], None],
        slug: str,
        data_source: str):
    """
        Transform data (dict, DTO or None) to a DTO class or a dict.
        This can be used to ensure you have the DTO (or dict) you expect.
        Specifying dto_class=None will convert data to a dict.

        It can also be used to create DTOs from model output that might be generic,
        for example models that call other models.

        Note that if you have a data structure such as a dict or list
        that contains DTOs, the transformation is not deep so the embedded
        values will remain as DTOs. In this case, to serialize the
        data you can use credmark.dto.json_dump or
        json_dumps.

        :param data: data in the form of a dict or DTO instance
        :param dto_class: DTO subclass (or None to convert to dict)
        :param slug: the slug of the calling model (used only for error messages)
        :param data_source: short string describing source of data,
                            ex "input" (used for error messages)
    """
    try:
        if dto_class is None:
            # Return a dict
            if data is None:
                # empty dict
                return {}
            if isinstance(data, DTOTypesTuple):
                # get dict from dto instance
                return data.dict()
            else:
                # return dict
                return data
        else:
            # Return a dto instance
            if data is None:
                # construct the dto with no data
                # This will be fine if the dto has default values,
                # otherwise it raises an exception which is caught below.
                return dto_class()  # type: ignore
            if isinstance(data, dto_class):
                # already the right dto class
                return data
            if isinstance(data, DTOTypesTuple):
                # convert one dto to another dto class
                return dto_class(**data.dict())  # type: ignore
            else:
                # create dto from dict
                return dto_class(**data)
    except Exception as e:
        raise DataTransformError(
            f'Error validating model {slug} {data_source}: {e}')
