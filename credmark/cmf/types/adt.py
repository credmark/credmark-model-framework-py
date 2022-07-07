# algebra data types

from typing import Generic, Iterator, List, Optional, TypeVar

import pandas as pd
from credmark.dto import DTOTypesTuple
from pydantic import Field as DTOField
from pydantic.generics import GenericModel as GenericDTO

DTOCLS = TypeVar('DTOCLS')


class Maybe(GenericDTO, Generic[DTOCLS]):
    just: Optional[DTOCLS] = DTOField(None)

    def is_just(self):
        return self.just is not None


class Many(GenericDTO, Generic[DTOCLS]):
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

    def to_dataframe(self):
        first_elem = self.some[0]
        if isinstance(first_elem, DTOTypesTuple):
            print('dto')
            data_dict = [x.dict() for x in self.some]  # type: ignore
        elif isinstance(first_elem, dict):
            print('dict')
            data_dict = self.some
        else:
            data_dict = [{0: x} for x in self.some]

        return pd.DataFrame(data_dict)
