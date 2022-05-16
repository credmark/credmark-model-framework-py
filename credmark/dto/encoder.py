import json
import datetime
import numpy as np
from credmark.dto import DTO


class PydanticJSONEncoder(json.JSONEncoder):
    """
    A JSON encoder that will handle DTO types embedded
    in other data structures such as dicts or lists.

    Use it as the cls passed to json dump(s):
      json.dump(result, cls=PydanticJSONEncoder)
    """

    def default(self, obj):
        if isinstance(obj, DTO):
            return obj.dict()
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)


def json_dump(obj, fp, **json_dump_args):  # pylint: disable=invalid-name
    """Dump an obj that may contain embedded DTOs to json"""
    return json.dump(obj, fp, cls=PydanticJSONEncoder, **json_dump_args)


def json_dumps(obj, **json_dump_args):
    """Dump an obj that may contain embedded DTOs to json string"""
    return json.dumps(obj, cls=PydanticJSONEncoder, **json_dump_args)
