
from typing import Type, Union
from .errors import ModelRunError
from ..types.dto import DTO


def transform_data_for_dto(
        data: Union[dict, DTO, None],
        dto_class: Union[Type[DTO], None],
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
        data you can use credmark.model.encoder.json_dump or
        json_dumps.

        :param data: data in the form of a dict or DTO instance
        :param dto_class: DTO subclass (or None to convert to dict)
        :param slug: the slug of the calling model (used for errors)
        :param data_source: short string describing source of data, ex "input" (used for errors)
    """
    try:
        if dto_class is None:
            # Return a dict
            if data is None:
                # empty dict
                return {}
            if isinstance(data, DTO):
                # get dict from dto instance
                return data.dict()
            else:
                # return dict
                return data
        else:
            # Return a dto instance
            if data is None:
                # construct the dto with no data
                # (which will be fine if the dto has default values)
                return dto_class()
            if isinstance(data, dto_class):
                # already the right dto class
                return data
            if isinstance(data, DTO):
                # convert one dto to another dto class
                return dto_class(**data.dict())
            else:
                # create dto from dict
                return dto_class(**data)
    except Exception as e:
        raise ModelRunError(
            f'Error validating model {slug} {data_source}: {e}, with data={data}')
