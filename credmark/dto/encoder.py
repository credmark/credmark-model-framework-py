import json
from credmark.dto import DTO


class PydanticJSONEncoder(json.JSONEncoder):
    """
    A JSON encoder that will handle DTO types embedded
    in other data structures such as dicts or lists.

    Use it as the cls passed to json dump(s):
      json.dump(result, cls=PydanticJSONEncoder)
    """

    def default(self, o):
        if isinstance(o, DTO):
            return o.dict()
        return json.JSONEncoder.default(self, o)


def json_dump(obj, handle, format_json=lambda x: x, **json_dump_args):
    """Dump an obj that may contain embedded DTOs to json"""
    return format_json(json.dump(obj, handle, cls=PydanticJSONEncoder, **json_dump_args))


def json_dumps(obj):
    """Dump an obj that may contain embedded DTOs to json string"""
    return json.dumps(obj, cls=PydanticJSONEncoder)
