import json
import datetime
import numpy as np
from credmark.dto import DTOTypesTuple


class PydanticJSONEncoder(json.JSONEncoder):
    """
    A JSON encoder that will handle DTO types embedded
    in other data structures such as dicts or lists.

    Use it as the cls passed to json dump(s):
      json.dump(result, cls=PydanticJSONEncoder)
    """

    def default(self, o):
        if isinstance(o, DTOTypesTuple):
            return o.dict()
        if isinstance(o, np.integer):
            return int(o)
        if isinstance(o, np.floating):
            return float(o)
        if isinstance(o, np.ndarray):
            return o.tolist()
        if isinstance(o, (datetime.date, datetime.datetime)):
            return o.isoformat()
        return json.JSONEncoder.default(self, o)


def json_dump(obj, fp, **json_dump_args):  # pylint: disable=invalid-name
    """Dump an o that may contain embedded DTOs to json"""
    return json.dump(obj, fp, cls=PydanticJSONEncoder, **json_dump_args)


def json_dumps(obj, **json_dump_args):
    """Dump an obj that may contain embedded DTOs to json string"""
    return json.dumps(obj, cls=PydanticJSONEncoder, **json_dump_args)
