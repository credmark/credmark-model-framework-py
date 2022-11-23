import datetime
import json

import numpy as np
from credmark.dto import DTO, DTOTypesTuple


class PydanticJSONEncoder(json.JSONEncoder):
    """
    A JSON encoder that will handle DTO types embedded
    in other data structures such as dicts or lists.

    Use it as the cls passed to json dump(s):
      json.dump(result, cls=PydanticJSONEncoder)
    """

    def encode(self, o) -> str:
        # A top-level primitive DTO (IntDTO, StrDTO, FloatDTO)
        # is serialized as a dict.
        if isinstance(o, DTOTypesTuple):
            o = o.dict()
        return super().encode(o)

    # pylint: disable=too-many-return-statements
    def default(self, o):
        # Primitive DTO types (IntDTO, StrDTO, FloatDTO) are
        # serialized as primitive types if not the top-level DTO.
        if isinstance(o, DTO):
            return o.dict()
        if isinstance(o, np.integer):
            return int(o)
        if isinstance(o, np.floating):
            if np.isnan(o):
                return None  # Serialized as JSON null.
            return float(o)
        if isinstance(o, np.ndarray):
            return o.tolist()
        if isinstance(o, np.bool_):
            return bool(o)
        if isinstance(o, (datetime.date, datetime.datetime)):
            return o.isoformat()
        return json.JSONEncoder.default(self, o)


def json_dump(obj, fp, **json_dump_args) -> None:  # pylint: disable=invalid-name
    """Dump an o that may contain embedded DTOs to json"""
    return json.dump(obj, fp, cls=PydanticJSONEncoder, **json_dump_args)


def json_dumps(obj, **json_dump_args) -> str:
    """Dump an obj that may contain embedded DTOs to json string"""
    return json.dumps(obj, cls=PydanticJSONEncoder, **json_dump_args)
