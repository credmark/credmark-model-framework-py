# pylint:disable=no-member, not-an-iterable, unsubscriptable-object

# algebra data types

from typing import Callable, Generic, Iterator, List, Optional, Tuple, TypeVar

import pandas as pd

from credmark.dto import DTOField, DTOTypesTuple, GenericDTO

DTOCLS = TypeVar('DTOCLS')


class Maybe(GenericDTO, Generic[DTOCLS]):
    just: Optional[DTOCLS] = DTOField(None)

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

    def is_empty(self) -> bool:
        return len(self.some) == 0

    @classmethod
    def empty(cls):
        return cls(some=[])

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
                data_dict = [{n: f(x) for n, f in fields}
                             for x in self.some]  # type: ignore
        elif isinstance(first_elem, dict):
            if fields is None:
                data_dict = self.some
            else:
                data_dict = [{n: f(x) for n, f in fields}
                             for x in self.some]  # type: ignore
        else:
            data_dict = [{0: x} for x in self.some]

        return pd.DataFrame(data_dict)

    def sorted(self, key=None, reverse=False):
        return sorted(self.some, key=key, reverse=reverse)  # type: ignore


class Records(GenericDTO):
    records: List[Tuple] = DTOField([])
    fields: List[str] = DTOField([], description='List of fields')
    n_rows: int
    fix_int_columns: List[str] = DTOField(
        [], description='List of int fields to be restored from string')
    _iterator: str = 'records'

    def __iter__(self) -> Iterator[Tuple]:
        return getattr(self, self._iterator).__iter__()

    def __getitem__(self, key) -> Tuple:
        return getattr(self, self._iterator).__getitem__(key)

    def is_empty(self) -> bool:
        return len(self.records) == 0

    @classmethod
    def empty(cls):
        return cls(records=[], fields=[], n_rows=0, fix_int_columns=[])

    def append(self, obj):
        return getattr(self, self._iterator).append(obj)

    def extend(self, obj):
        return getattr(self, self._iterator).extend(obj)

    def __len__(self) -> int:
        return len(self.records)

    def to_dataframe(self):
        if len(self.records) == 0:
            return pd.DataFrame(columns=self.fields, data=[])

        data_dict = [dict(zip(self.fields, r)) for r in self.records]
        df_in = pd.DataFrame(data_dict)
        if len(self.fix_int_columns) > 0:
            for field in self.fix_int_columns:
                df_in = df_in.assign(
                    value=lambda x, field=field: x[field].apply(int))
        return df_in

    @classmethod
    def from_dataframe(cls, _df, fix_int_columns=None):  # pylint:disable=dangerous-default-value
        return cls(records=list(_df.itertuples(index=False, name=None)),
                   fields=_df.columns.tolist(),
                   n_rows=_df.shape[0],
                   fix_int_columns=[] if fix_int_columns is None else fix_int_columns)
