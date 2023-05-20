# pylint:disable=no-member, line-too-long

import contextlib
from enum import Enum
from typing import Optional, Tuple, Union

import credmark.cmf.model

from .ledger import ColumnField, JoinType, LedgerAggregate, LedgerJoin, LedgerModelOutput, LedgerTable
from .ledger_errors import InvalidQueryException


# pylint: disable=locally-disabled,invalid-name, too-many-arguments
class LedgerQueryBase(contextlib.AbstractContextManager):
    # Duplicated from credmark/cmf/types/ledger.py for easy access from context
    class JoinType(str, Enum):
        INNER = 'inner'
        LEFT_OUTER = 'leftOuter'
        RIGHT_OUTER = 'rightOuter'
        FULL_OUTER = 'fullOuter'
        CROSS = 'cross'
        NATURAL = 'natural'

    def __enter__(self):
        return self

    def __exit__(self, *_exc):
        return None

    def __init__(self):
        pass

    @classmethod
    def field(cls, value):
        return ColumnField(value)

    # pylint: disable=too-many-locals
    def _gen_model_input(self,
                         model_slug: str,
                         originator: str,
                         columns: Optional[Union[list[str], list[ColumnField]]] = None,
                         joins: Optional[list[Union[tuple[JoinType, LedgerTable, str], tuple[LedgerTable, str]]]] = None,
                         where: Optional[str] = None,
                         group_by: Optional[Union[list[str], list[ColumnField]]] = None,
                         order_by: Optional[Union[str, ColumnField]] = None,
                         limit: Optional[int] = None,
                         offset: Optional[int] = None,
                         aggregates: Optional[list[Tuple[str, str]]] = None,
                         having: Optional[str] = None) -> dict:

        aggregates_names = [agg[0] for agg in aggregates] if aggregates else []

        if group_by is not None:
            if columns == []:
                columns = None
            if columns is not None:
                raise InvalidQueryException(
                    model_slug,
                    (f'{model_slug} call with group_by will need the columns to be '
                     'empty [] or None.'))
            columns = [c for c in group_by
                       if c in self.columns and c not in aggregates_names]  # type: ignore

        if not columns and not aggregates:
            raise InvalidQueryException(
                model_slug, f'{model_slug} call must have at least one column or aggregate.')

        if columns is None:
            columns = []
        elif not isinstance(columns, list):
            raise InvalidQueryException(
                model_slug, f'{columns=} needs to be a list of string.')
        else:
            self._validate_columns(  # type: ignore
                model_slug, columns)

        if where is None and limit is None and not aggregates:
            raise InvalidQueryException(
                model_slug,
                f'{model_slug} call must have a where or limit value for non-aggregate queries.')

        if limit is not None and (not isinstance(limit, int) or limit < 0):
            raise InvalidQueryException(
                model_slug,
                f'{limit=} needs to be a positive integer.')

        if offset is not None and (not isinstance(offset, int) or offset < 0):
            raise InvalidQueryException(
                model_slug,
                f'{offset=} needs to be a positive integer.')

        # Fix for contract ledger
        # Customized columns needs to be converted to string to avoid losing precision.
        # https://github.com/credmark/credmark-model-runner-api/issues/50
        cols_customized = [(f'{c}::TEXT', c)
                           for c in columns if c in self.bigint_cols]  # type: ignore

        columns = [c for c in columns
                   if c not in self.bigint_cols]  # type: ignore

        aggregates_list = (
            [] if aggregates is None else aggregates) + cols_customized
        aggregates_value = (None if len(aggregates_list) == 0
                            else [LedgerAggregate(expression=agg[0], asName=agg[1])
                                  for agg in aggregates_list])

        joins_value = [LedgerJoin(tableKey=table.table_key,
                                  alias=table.alias,
                                  on=on,
                                  type=(type_list[0] if type_list else None))  # type: ignore
                       for (*type_list, table, on) in joins] if joins is not None else None

        return {'alias': getattr(self, 'alias', None),
                'columns': columns,
                'joins': joins_value,
                'aggregates': aggregates_value,
                'where': where,
                'groupBy': ','.join(group_by) if group_by is not None else None,
                'having': having,
                'orderBy': order_by,
                'limit': str(limit) if limit is not None else None,
                'offset': str(offset) if offset is not None else None,
                'originator': originator
                }


# pylint: disable=too-many-arguments, protected-access
class LedgerQuery(LedgerQueryBase):
    def __init__(self, **kwargs):
        super().__init__()
        self._cwgo_query = kwargs['cwgo_query_table']

    def select(self,
               columns: Optional[Union[list[str], list[ColumnField]]] = None,
               joins: Optional[list[Union[tuple[JoinType, LedgerTable, str], tuple[LedgerTable, str]]]] = None,
               where: Optional[str] = None,
               group_by: Optional[Union[list[str], list[ColumnField]]] = None,
               order_by: Optional[Union[str, ColumnField]] = None,
               limit: Optional[int] = None,
               offset: Optional[int] = None,
               aggregates: Optional[list[tuple[str, str]]] = None,
               having: Optional[str] = None,
               bigint_cols: Optional[list[str]] = None) -> LedgerModelOutput:
        """
        Query data from the table.
        """
        context = credmark.cmf.model.ModelContext.current_context()
        model_input = self._gen_model_input(
            model_slug=self._cwgo_query,
            originator=context.__dict__['slug'],
            columns=columns,
            joins=joins,
            where=where,
            group_by=group_by,
            order_by=order_by,
            limit=limit,
            offset=offset,
            aggregates=aggregates,
            having=having)

        ledger_out = context.run_model(slug=self._cwgo_query,
                                       input=model_input,
                                       return_type=LedgerModelOutput)
        ledger_out.set_bigint_cols(
            self.bigint_cols +  # type: ignore
            ([] if bigint_cols is None else bigint_cols))
        return ledger_out
