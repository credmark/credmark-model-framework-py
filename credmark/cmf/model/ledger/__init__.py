import contextlib
from typing import Type, Union, List

from .errors import (
    InvalidColumnException,
    InvalidQueryException,
)

from credmark.cmf.types.ledger import (
    BlockTable, ContractTable,
    LogTable, ReceiptTable, TokenTable, TokenTransferTable,
    TraceTable, TransactionTable, LedgerTable,
    LedgerAggregate, LedgerModelOutput
)


QUERY_METHOD_DOC_STRING = """

    Columns are defined in :class:`credmark.cmf.types.ledger.{TABLE}Table.Columns` which
    is also accessible as ``Ledger.{TABLE}.Columns``

    Parameters:

        columns: The columns list should be built using ``Ledger.{TABLE}.Columns``

        aggregates: The aggregates list should be built using ``Ledger.Aggregate()``
            calls where the expression contains an SQL function(ex. MAX, SUM etc.) and
            column names are from ``Ledger.{TABLE}.Columns``.

        where: The where portion of an SQL query(without the word WHERE.)
            The column names are from ``Ledger.{TABLE}.Columns``.
            Aggregate column names must be in double-quotes.

        group_by: The "group by" portion of an SQL query(without the words "GROUP BY".)
            The column names are from ``Ledger.{TABLE}.Columns``.
            Aggregate column names must be in double-quotes.

        order_by: The "order by" portion of an SQL query(without the words "ORDER BY".)
            The column names are from ``Ledger.{TABLE}.Columns``.
            Aggregate column names must be in double-quotes.

        having: The "having" portion of an SQL query(without the word "HAVING".)
            The column names are from ``Ledger.{TABLE}.Columns``.
            Aggregate column names must be in double-quotes.

        limit: The "limit" portion of an SQL query(without the word "LIMIT".)
            Typically this can be an integer as a string.

        offset: The "offset" portion of an SQL query(without the word "OFFSET".)
            Typically this can be an integer as a string.

    Returns:
        An object with a ``data`` property which is a list
        of dicts, each dict holding a row with the keys being the column
        names. The column names can be referenced using
        ``Ledger.{TABLE}.Columns`` and aggregate columns names.
    """


def query_method(func):
    def wrapper(self, *args, **kwargs):
        func.__doc__ += QUERY_METHOD_DOC_STRING
        func.__doc__ = func.__doc__.replace('{TABLE}', self.table_name)
        return func(self, *args, **kwargs)
    return wrapper


class LedgerQuery(contextlib.AbstractContextManager):
    # pylint: disable=locally-disabled,invalid-name
    def __init__(self, ledger_table, table_name, cwgo_query_table, context):
        self._ledger_table = ledger_table
        self._table_name = table_name
        self._cwgo_query = cwgo_query_table
        self._context = context

    @property
    def table_name(self):
        return self._table_name

    @property
    def Columns(self):
        return self._ledger_table.Columns

    def columns(self):
        return self._ledger_table.columns()

    def _validate_columns(self, model_slug: str,
                          columns: List[str]):
        column_set = self._ledger_table.columns()

        if column_set is not None:
            for column in columns:
                if column.lower() not in column_set:
                    raise InvalidColumnException(
                        model_slug,
                        column, list(column_set), "invalid column name")

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
            self._validate_columns(model_slug, columns)

        if where is None and limit is None and not aggregates:
            raise InvalidQueryException(
                model_slug,
                f'{model_slug} call must have a where or limit value for non-aggregate queries.')

        model_input = {'columns': columns, 'aggregates': aggregates,
                       'where': where, 'groupBy': group_by,
                       'having': having, 'orderBy': order_by,
                       'limit': limit, 'offset': offset}

        return self.context.run_model(model_slug,
                                      model_input,
                                      return_type=LedgerModelOutput)

    @query_method
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

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return None


class Ledger:
    """
    Performs queries on ledger data.

    Access an instance of this class from the model context using
    ``self.context.ledger``.

    Run a query using one of the ``get_`` methods, for example
    ``context.ledger.get_transactions()``. The query parameters are
    common to all query methods.

    """
    # pylint: disable=locally-disabled,invalid-name
    @classmethod
    def Aggregate(cls, expression: str, as_name: str):
        """
        Return a new LedgerAggregate instance that can be used in
        an aggregates list.

        For example: :

            aggregates = [Ledger.Aggregate(f'SUM({Ledger.Block.Columns.GAS_USED})', 'total_gas')]
        """
        return LedgerAggregate(expression=expression, asName=as_name)

    def __init__(self, context):
        # We type the property here to avoid circular ref
        self.context = context
        self.Transaction = LedgerQuery(TransactionTable, 'Transaction',
                                       'ledger.transaction_data', self.context)
        self.Trace = LedgerQuery(TraceTable, 'Trace', 'ledger.trace_data', context)
        self.Block = LedgerQuery(BlockTable, 'Block', 'ledger.block_data', context)
        self.Contract = LedgerQuery(ContractTable, 'Contract', 'ledger.contract_data', context)
        self.Log = LedgerQuery(LogTable, 'Log', 'ledger.log_data', context)
        self.Receipt = LedgerQuery(ReceiptTable, 'Receipt', 'ledger.receipt_data', context)
        self.Token = LedgerQuery(TokenTable, 'Token', 'ledger.erc20_token_data', context)
        self.TokenTransfer = LedgerQuery(TokenTransferTable, 'TokenTransfer',
                                         'ledger.erc20_token_transfer_data', context)
