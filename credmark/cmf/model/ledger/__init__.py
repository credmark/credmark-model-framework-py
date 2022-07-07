from credmark.cmf.types.ledger import (BlockTable, ContractTable, LogTable,
                                       ReceiptTable, TokenBalanceTable,
                                       TokenTable, TokenTransferTable,
                                       TraceTable, TransactionTable)
from credmark.cmf.types.ledger_query import LedgerQuery

QUERY_METHOD_DOC_STRING = """
    Columns are defined in :class:`credmark.cmf.types.ledger.{TABLE}Table`
    which is also accessible as
    - ``context.Ledger.{TABLE}.colnames()`` for the names to specify in the query, and
    - ``context.Ledger.{TABLE}.columns()`` to include them all.

    Parameters:

        columns: The columns list should be built using ``Ledger.{TABLE}``

        aggregates: The aggregates list should be built using
            tuples of [expression, name] to be processed by `Ledger.Aggregate()`.
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
            Typically this can be an integer.

        offset: The "offset" portion of an SQL query(without the word "OFFSET".)
            Typically this can be an integer.

    Returns:
        An object with a ``data`` property which is a list
        of dicts, each dict holding a row with the keys being the column
        names. The column names can be referenced using
        ``Ledger.{TABLE}`` and aggregate columns names.
    """


def ledger_table_doc(func):
    def wrapper(self, *args, **kwargs):
        func.__doc__ = QUERY_METHOD_DOC_STRING.replace('{TABLE}', func.__name__)
        result = func(self, *args, **kwargs)
        result.__doc__ = QUERY_METHOD_DOC_STRING.replace('{TABLE}', func.__name__)
        return result
    return wrapper


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


class LedgerQueryTokenBalance(TokenBalanceTable, LedgerQuery):
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
    @ledger_table_doc
    def Transaction(self):
        return LedgerQueryTransaction(
            cwgo_query_table='ledger.transaction_data',
            context=self._context, more_cols=[])

    @property
    @ledger_table_doc
    def Trace(self):
        return LedgerQueryTrace(
            cwgo_query_table='ledger.trace_data',
            context=self._context, more_cols=[])

    @property
    @ledger_table_doc
    def Block(self):
        return LedgerQueryBlock(
            cwgo_query_table='ledger.block_data',
            context=self._context, more_cols=[])

    @property
    @ledger_table_doc
    def Contract(self):
        return LedgerQueryContract(
            cwgo_query_table='ledger.contract_data',
            context=self._context, more_cols=[])

    @property
    @ledger_table_doc
    def Log(self):
        return LedgerQueryLog(
            cwgo_query_table='ledger.log_data',
            context=self._context, more_cols=[])

    @property
    @ledger_table_doc
    def Receipt(self):
        return LedgerQueryReceipt(
            cwgo_query_table='ledger.receipt_data',
            context=self._context, more_cols=[])

    @property
    @ledger_table_doc
    def Token(self):
        return LedgerQueryToken(
            cwgo_query_table='ledger.erc20_token_data',
            context=self._context, more_cols=[])

    @property
    @ledger_table_doc
    def TokenTransfer(self):
        return LedgerQueryTokenTransfer(
            cwgo_query_table='ledger.erc20_token_transfer_data',
            context=self._context, more_cols=[])

    @property
    @ledger_table_doc
    def TokenBalance(self):
        return LedgerQueryTokenBalance(
            cwgo_query_table='ledger.token_balance',
            context=self._context, more_cols=[])
