import json
import os
from typing import Any, Dict, List


class ABI(list):
    class EventDetails:
        def __init__(self, name, args, types):
            self._name = name
            self._args = args
            self._types = types

        def __str__(self) -> str:
            return (f'Event Name: {self._name}{os.linesep}'
                    f'Args: {self._args}{os.linesep}'
                    f'Types: {self._types}')

        def __repr__(self) -> str:
            return self.__str__()

        @ property
        def args(self) -> List[str]:
            return self._args

        @ property
        def types(self) -> List[str]:
            return self._types

    class FuncDetails(EventDetails):
        def __init__(self, name, args, types, output):
            super().__init__(name, args, types)
            self._output = output

        def __str__(self) -> str:
            return (f'Function Name: {self._name}{os.linesep}'
                    f'Args: {self._args}{os.linesep}'
                    f'Types: {self._types}{os.linesep}'
                    f'Output: {self._output}')

        @ property
        def output(self) -> List[str]:
            return self._output

    class Funcs:
        NAME: str = "Functions"

        def __init__(self, abi: Dict[str, dict]):
            self._abi = abi
            self._names = list(abi.keys())

        def __len__(self):
            return len(self._names)

        def __contains__(self, _names):
            return _names.upper() in [x.upper() for x in self._names]

        def __dir__(self):
            return self._names

        def __repr__(self):
            return f'{self.NAME}: [{", ".join(self._names)}]'

        def __str__(self):
            return self.__repr()

        def __getitem__(self, name: str):
            if name in self:
                return [v for k, v in self._abi.items()
                        if k.upper() == name.upper()][0]
            else:
                return None

        def __getattr__(self, _name: str) -> Any:
            entry = self[_name]
            if entry is not None:
                inputs = entry['inputs']
                args = [x['name'] if 'name' in x else None for x in inputs]
                types = [x['type'] if 'type' in x else None for x in inputs]
                outputs = [x['type'] if 'type' in x else None for x in entry['outputs']]
                return ABI.FuncDetails(_name, args, types, outputs)
            return None

    class Events(Funcs):
        NAME: str = "Events"

        def __init__(self, abi: Dict[str, dict]):
            super().__init__(abi)

        def __getattr__(self, _name: str) -> Any:
            entry = self[_name]
            if entry is not None:
                entry = self._abi[_name]
                inputs = entry['inputs']
                args = [x['name'] for x in inputs]
                types = [x['type'] for x in inputs]
                return ABI.EventDetails(_name, args, types)
            return None

    def __init__(self, abi=None):
        if abi is None:
            abi = []
        elif isinstance(abi, str):
            abi = json.loads(abi)
        super().__init__(abi)
        self._functions = ABI.Funcs({})
        self._events = ABI.Events({})

    @ property
    def functions(self):
        if len(self._functions) == 0:
            self._functions = ABI.Funcs(
                {v['name']: v
                 for v in self
                 if 'type' in v and 'name' in v and v['type'] == 'function'})
        return self._functions

    @ property
    def events(self):
        if len(self._events) == 0:
            self._events = ABI.Events(
                {v['name']: v
                 for v in self
                 if 'type' in v and 'name' in v and v['type'] == 'event'})
        return self._events
