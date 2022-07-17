# algebra data types

from typing import Callable, Generic, Iterator, List, Optional, Tuple, TypeVar

import pandas as pd
from credmark.dto import DTOField, DTOTypesTuple, GenericDTO

DTOCLS = TypeVar('DTOCLS')


class Maybe(GenericDTO, Generic[DTOCLS]):
    just: Optional[DTOCLS] = DTOField(None)

    def is_just(self):
        return self.just is not None

    def get_just(self, obj: DTOCLS) -> DTOCLS:
        return self.just if self.just is not None else obj

    @classmethod
    def none(cls):
        return cls(just=None)


class Some(GenericDTO, Generic[DTOCLS]):
    some: List[DTOCLS] = DTOField([])
    _iterator: str = 'some'

    def __iter__(self) -> Iterator[DTOCLS]:
        return getattr(self, self._iterator).__iter__()

    def __getitem__(self, key) -> DTOCLS:
        return getattr(self, self._iterator).__getitem__(key)

    def append(self, obj):
        return getattr(self, self._iterator).append(obj)

    def extend(self, obj):
        return getattr(self, self._iterator).extend(obj)

    def __len__(self) -> int:
        return len(self.some)

    def to_dataframe(self, fields: Optional[List[Tuple[str, Callable]]] = None):
        if len(self.some) == 0:
            return pd.DataFrame()

        first_elem = self.some[0]
        if isinstance(first_elem, DTOTypesTuple):
            if fields is None:
                data_dict = [x.dict() for x in self.some]  # type: ignore
            else:
                data_dict = [{n: f(x) for n, f in fields} for x in self.some]  # type: ignore
        elif isinstance(first_elem, dict):
            if fields is None:
                data_dict = self.some
            else:
                data_dict = [{n: f(x) for n, f in fields} for x in self.some]  # type: ignore
        else:
            data_dict = [{0: x} for x in self.some]

        return pd.DataFrame(data_dict)
