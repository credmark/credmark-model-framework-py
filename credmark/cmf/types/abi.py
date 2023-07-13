import json
import os
from collections import UserList
from typing import Dict, List, Union


class EventDetails:
    def __init__(self, name, args, types, raw_abi):
        self._name = name
        self._args = args
        self._types = types
        self._raw_abi = raw_abi

    def __str__(self) -> str:
        return (f'Event Name: {self._name}{os.linesep}'
                f'Args: {self._args}{os.linesep}'
                f'Types: {self._types}')

    def __repr__(self) -> str:
        return self.__str__()

    @property
    def args(self) -> List[str]:
        return self._args

    @property
    def types(self) -> List[str]:
        return self._types

    @property
    def raw_abi(self):
        return self._raw_abi


class FuncDetails(EventDetails):
    def __init__(self, name, args, types, output, raw_abi):
        super().__init__(name, args, types, raw_abi)
        self._output = output

    def __str__(self) -> str:
        return (f'Function Name: {self._name}{os.linesep}'
                f'Args: {self._args}{os.linesep}'
                f'Types: {self._types}{os.linesep}'
                f'Output: {self._output}')

    @property
    def output(self) -> List[str]:
        return self._output


class Events(UserList):
    NAME: str = "Events"

    def __init__(self, abi: Dict[str, dict]):
        self._abi = abi
        self._names = list(abi.keys())
        super().__init__(self._names)

    def __len__(self):
        return len(self._names)

    def __contains__(self, _name):
        if isinstance(_name, str):
            return _name.upper() in [x.upper() for x in self._names]
        return False

    def __dir__(self):
        return self._names

    def __repr__(self):
        return f'{self.NAME}: [{", ".join(self._names)}]'

    def __str__(self):
        return self.__repr__()

    @property
    def raw_abi(self):
        return self._abi

    def names(self):
        return dir(self)

    def _ipython_key_completions_(self):
        return dir(self)

    def __getitem__(self, name: str) -> dict:
        if isinstance(name, str):
            if name in self:
                return [v for k, v in self._abi.items()
                        if k.upper() == name.upper()][0]
            else:
                return {}
        else:
            return super().__getitem__(name)

    def __getattr__(self, _name: str) -> EventDetails:
        entry = self[_name]
        if len(entry.keys()) > 0:
            raw_abi = [v for k, v in self._abi.items() if k == _name]
            inputs = entry['inputs']
            args = [x['name'] for x in inputs]
            types = [x['type'] for x in inputs]
            return EventDetails(_name, args, types, raw_abi)
        return EventDetails(_name + ' (undefined)', [], [], [])


class Funcs(Events):
    NAME: str = "Functions"

    def __init__(self, abi: Dict[str, dict]):
        super().__init__(abi)

    def __getattr__(self, _name: str) -> FuncDetails:
        entry = self[_name]
        if len(entry.keys()) > 0:
            raw_abi = [v for k, v in self._abi.items() if k == _name]
            inputs = entry['inputs']
            args = [x['name'] if 'name' in x else None for x in inputs]
            types = [x['type'] if 'type' in x else None for x in inputs]
            outputs = [x['type'] if 'type' in x else None for x in entry['outputs']]
            return FuncDetails(_name, args, types, outputs, raw_abi)
        return FuncDetails(_name + ' (undefined)', [], [], [], [])


class ABI(list):
    def __init__(self, abi: Union[List, str, None] = None):
        if isinstance(abi, str):
            self._abi = json.loads(abi)
        else:
            self._abi = abi
        super().__init__([] if not self._abi else self._abi)
        self._functions = Funcs({})
        self._events = Events({})
        self.__loaded_events = False
        self.__loaded_functions = False

    def __dir__(self):
        return ['functions', 'events', 'find_events', 'find_functions']

    @property
    def functions(self):
        if not self.__loaded_functions:
            self._functions = Funcs(
                {v['name']: v
                 for v in self
                 if 'type' in v and 'name' in v and v['type'] == 'function'})
            self.__loaded_functions = True
        return self._functions

    @property
    def events(self):
        if not self.__loaded_events:
            self._events = Events(
                {v['name']: v
                 for v in self
                 if 'type' in v and 'name' in v and v['type'] == 'event'})
            self.__loaded_events = True
        return self._events
