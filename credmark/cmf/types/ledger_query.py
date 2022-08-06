import contextlib
from typing import List, Tuple, Union

import credmark.cmf.model

from .ledger import ColumnField, LedgerAggregate, LedgerModelOutput
from .ledger_errors import InvalidQueryException


class LedgerQueryBase(contextlib.AbstractContextManager):
    def __enter__(self):
        return self

    def __exit__(self, *_exc):
        return None

    # pylint: disable=locally-disabled,invalid-name
    def __init__(self):
        pass

    @classmethod
    def field(cls, value):
        return ColumnField(value)

    def _gen_model_input(self,  # pylint: disable=too-many-arguments
                         model_slug: str,
                         columns: Union[List[str], List[ColumnField], None] = None,
                         where: Union[str, None] = None,
                         group_by: Union[List[str], List[ColumnField], None] = None,
                         order_by: Union[str, ColumnField, None] = None,
                         limit: Union[int, None] = None,
                         offset: Union[int, None] = None,
                         aggregates: Union[List[Tuple[str, str]], None] = None,
                         having: Union[str, None] = None) -> dict:

        if group_by is not None:
            if columns is not None:
                raise InvalidQueryException(
                    model_slug,
                    f'{model_slug} call with group_by will need the columns to be empty.')
            # pylint:disable=no-member
            columns = [c for c in group_by
                       if c in self.columns]  # type: ignore

        if not columns and not aggregates:
            raise InvalidQueryException(
                model_slug, f'{model_slug} call must have at least one column or aggregate.')

        if columns is None:
            columns = []
        elif not isinstance(columns, list):
            raise InvalidQueryException(
                model_slug, f'{columns=} needs to be a list of string.')
        else:
            self._validate_columns(model_slug, columns)  # type: ignore # pylint:disable=no-member

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
        cols_customized = [(f'to_char({c})', c) for c in columns if c.startswith('inp_')]
        columns = [c for c in columns if not c.startswith('inp_')]

        aggregates = ([] if aggregates is None else aggregates) + cols_customized
        aggregates_value = (None if len(aggregates) == 0
                            else [LedgerAggregate(expression=agg[0], asName=agg[1])
                                  for agg in aggregates])

        model_input = {'columns': columns,
                       'aggregates': aggregates_value,
                       'where': where,
                       'groupBy': ','.join(group_by) if group_by is not None else None,
                       'having': having,
                       'orderBy': order_by,
                       'limit': str(limit) if limit is not None else None,
                       'offset': str(offset) if offset is not None else None}
        return model_input


class LedgerQuery(LedgerQueryBase):

    def __init__(self, **kwargs):
        super().__init__()
        self._cwgo_query = kwargs['cwgo_query_table']

    def select(self,  # pylint: disable=too-many-arguments
               columns: Union[List[str], List[ColumnField], None] = None,
               where: Union[str, None] = None,
               group_by: Union[List[str], List[ColumnField], None] = None,
               order_by: Union[str, ColumnField, None] = None,
               limit: Union[int, None] = None,
               offset: Union[int, None] = None,
               aggregates: Union[List[Tuple[str, str]], None] = None,
               having: Union[str, None] = None) -> LedgerModelOutput:
        """
        Query data from the table.
        """
        model_input = self._gen_model_input(model_slug=self._cwgo_query,
                                            columns=columns,
                                            where=where,
                                            group_by=group_by,
                                            order_by=order_by,
                                            limit=limit,
                                            offset=offset,
                                            aggregates=aggregates,
                                            having=having)

        context = credmark.cmf.model.ModelContext.current_context()
        return context.run_model(slug=self._cwgo_query,
                                 input=model_input,
                                 return_type=LedgerModelOutput)
