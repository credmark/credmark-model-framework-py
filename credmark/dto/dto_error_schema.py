
from typing import List, Tuple


def extract_error_codes_and_descriptions(error_schema: dict):
    result: List[Tuple[str, List[str], str]] = []
    definitions = error_schema.get('definitions')
    if definitions is not None:
        for _k, v in definitions.items():
            props = v.get('properties')
            if props is not None:
                code = props.get('code')
                if code is not None and 'enum' in code:
                    err_type = props.get('type')
                    err_type_d = err_type.get(
                        'description') if err_type is not None else None
                    err_type_d = err_type_d if err_type_d is not None else 'ModelError'
                    result.append((err_type_d, code.get('enum'), code.get('description')))
    return result
