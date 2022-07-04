import contextlib
from typing import List, Tuple, Type, Union

from matplotlib.style import context

from credmark.cmf.types.ledger import (BlockTable, ContractTable,
                                       LedgerAggregate, LedgerModelOutput,
                                       LedgerTable, LogTable, ReceiptTable,
                                       TokenTable, TokenTransferTable,
                                       TraceTable, TransactionTable)

from .errors import InvalidQueryException

QUERY_METHOD_DOC_STRING = """
    Columns are defined in :class:`credmark.cmf.types.ledger.{TABLE}Table`
    which is also accessible as
    - ``context.Ledger.{TABLE}.colnames()`` for the names to specify in the query, and
    - ``context.Ledger.{TABLE}.columns()`` to include them all.

    Parameters:

        columns: The columns list should be built using ``Ledger.{TABLE}``

        aggregates: The aggregates list should be built using ``Ledger.Aggregate()``
            calls where the expression contains an SQL function(ex. MAX, SUM etc.) and
            column names are from ``Ledger.{TABLE}``.

        where: The where portion of an SQL query(without the word WHERE.)
            The column names are from ``Ledger.{TABLE}``.
            Aggregate column names must be in double-quotes.

        group_by: The "group by" portion of an SQL query(without the words "GROUP BY".)
            The column names are from ``Ledger.{TABLE}``.
            Aggregate column names must be in double-quotes.

        order_by: The "order by" portion of an SQL query(without the words "ORDER BY".)
            The column names are from ``Ledger.{TABLE}``.
            Aggregate column names must be in double-quotes.

        having: The "having" portion of an SQL query(without the word "HAVING".)
            The column names are from ``Ledger.{TABLE}``.
            Aggregate column names must be in double-quotes.

        limit: The "limit" portion of an SQL query(without the word "LIMIT".)
            Typically this can be an integer as a string.

        offset: The "offset" portion of an SQL query(without the word "OFFSET".)
            Typically this can be an integer as a string.

    Returns:
        An object with a ``data`` property which is a list
        of dicts, each dict holding a row with the keys being the column
        names. The column names can be referenced using
        ``Ledger.{TABLE}`` and aggregate columns names.
    """


def query_method(func):
    def wrapper(self, *args, **kwargs):
        func.__doc__ = QUERY_METHOD_DOC_STRING.replace('{TABLE}', func.__name__)
        result = func(self, *args, **kwargs)
        # result.__doc__ = QUERY_METHOD_DOC_STRING.replace('{TABLE}', func.__name__)
        return result
    return wrapper


class LedgerQuery(contextlib.AbstractContextManager):
    _ledger_table_type = LedgerTable

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return None

    # pylint: disable=locally-disabled,invalid-name

    def __init__(self, **kwargs):
        self._table_name = kwargs['table_name']
        self._cwgo_query = kwargs['cwgo_query_table']
        self._context = kwargs['context']
        print(f'{self.__class__.__name__}__init__')

    @classmethod
    def Aggregate(cls, expression: str, as_name: str):
        """
        Return a new LedgerAggregate instance that can be used in
        an aggregates list.

        For example: :

            aggregates = [Ledger.Aggregate(f'SUM({Ledger.Block.GAS_USED})', 'total_gas')]
        """
        return LedgerAggregate(expression=expression, asName=as_name)

    def _send_cwgo_query(self,  # pylint: disable=too-many-arguments
                         model_slug: str,
                         columns: Union[List[str], None] = None,
                         where: Union[str, None] = None,
                         group_by: Union[str, None] = None,
                         order_by: Union[str, None] = None,
                         limit: Union[str, None] = None,
                         offset: Union[str, None] = None,
                         aggregates: Union[List[LedgerAggregate], None] = None,
                         having: Union[str, None] = None) -> LedgerModelOutput:
        if not columns and not aggregates:
            raise InvalidQueryException(
                model_slug, f'{model_slug} call must have at least one column or aggregate.')

        if columns is None:
            columns = []
        elif not isinstance(columns, list):
            raise InvalidQueryException(
                model_slug, f'{columns} needs to be a list of string.')
        else:
            self._validate_columns(model_slug, columns)  # type: ignore # pylint:disable=no-member

        if where is None and limit is None and not aggregates:
            raise InvalidQueryException(
                model_slug,
                f'{model_slug} call must have a where or limit value for non-aggregate queries.')

        model_input = {'columns': columns, 'aggregates': aggregates,
                       'where': where, 'groupBy': group_by,
                       'having': having, 'orderBy': order_by,
                       'limit': limit, 'offset': offset}

        return self._context.run_model(model_slug,
                                       model_input,
                                       return_type=LedgerModelOutput)

    def select(self,  # pylint: disable=too-many-arguments
               columns: Union[List[str], None] = None,
               where: Union[str, None] = None,
               group_by: Union[str, None] = None,
               order_by: Union[str, None] = None,
               limit: Union[str, None] = None,
               offset: Union[str, None] = None,
               aggregates: Union[List[LedgerAggregate], None] = None,
               having: Union[str, None] = None) -> LedgerModelOutput:
        """
        Query data from the {TABLE} table.
        """
        return self._send_cwgo_query(self._cwgo_query,
                                     columns, where, group_by,
                                     order_by, limit, offset,
                                     aggregates, having)


class LedgerQueryTransaction(TransactionTable, LedgerQuery):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class LedgerQueryTrace(TraceTable, LedgerQuery):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class LedgerQueryBlock(BlockTable, LedgerQuery):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class LedgerQueryContract(ContractTable, LedgerQuery):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class LedgerQueryLog(LogTable, LedgerQuery):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class LedgerQueryReceipt(ReceiptTable, LedgerQuery):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class LedgerQueryToken(TokenTable, LedgerQuery):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class LedgerQueryTokenTransfer(TokenTransferTable, LedgerQuery):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Ledger:
    """
    Performs queries on ledger data.

    Access an instance of this class from the model context using
    ``self.context.ledger``.

    Get a query handle by the name of the ledger table, for example
    ``context.ledger.Transaction`` or ``context.ledger.Contract``.
    The query parameters are common to all query methods.

    """
    # pylint: disable=locally-disabled,invalid-name

    def __init__(self, _context):
        # We type the property here to avoid circular ref
        self._context = _context

    @property
    @query_method
    def Transaction(self):
        return LedgerQueryTransaction(table_name='Transaction',
                                      cwgo_query_table='ledger.transaction_data',
                                      context=self._context, more_cols=[])

    @property
    @query_method
    def Trace(self):
        return LedgerQueryTrace(table_name='Trace',
                                cwgo_query_table='ledger.trace_data',
                                context=self._context, more_cols=[])

    @property
    @query_method
    def Block(self):
        return LedgerQueryBlock(table_name='Block',
                                cwgo_query_table='ledger.block_data',
                                context=self._context, more_cols=[])

    @property
    @query_method
    def Contract(self):
        return LedgerQueryContract(table_name='Contract',
                                   cwgo_query_table='ledger.contract_data',
                                   context=self._context, more_cols=[])

    @property
    @query_method
    def Log(self):
        return LedgerQueryLog(table_name='Log',
                              cwgo_query_table='ledger.log_data',
                              context=self._context, more_cols=[])

    @property
    @query_method
    def Receipt(self):
        return LedgerQueryReceipt(table_name='Receipt',
                                  cwgo_query_table='ledger.receipt_data',
                                  context=self._context, more_cols=[])

    @property
    @query_method
    def Token(self):
        return LedgerQueryToken(table_name='Token',
                                cwgo_query_table='ledger.erc20_token_data',
                                context=self._context, more_cols=[])

    @property
    @query_method
    def TokenTransfer(self):
        return LedgerQueryTokenTransfer(table_name='TokenTransfer',
                                        cwgo_query_table='ledger.erc20_token_transfer_data',
                                        context=self._context, more_cols=[])
