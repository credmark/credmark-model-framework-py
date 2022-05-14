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


def _query_method(table: str):
    # decorator for a query method in the ledger that adds
    # docstrings based on a template.
    def _doc(func):
        func.__doc__ = func.__doc__.strip() + QUERY_METHOD_DOC_STRING.replace('{TABLE}', table)
        return func
    return _doc


class Ledger:
    """
    Performs queries on ledger data and has aliases to table definitions.

    Access an instance of this class from the model context using
    ``self.context.ledger``.

    Run a query using one of the ``get_`` methods, for example
    ``context.ledger.get_transactions()``. The query parameters are
    common to all query methods.

    """

    Transaction = TransactionTable
    """"""
    Trace = TraceTable
    """"""
    Block = BlockTable
    """"""
    Contract = ContractTable
    """"""
    Log = LogTable
    """"""
    Receipt = ReceiptTable
    """"""
    Token = TokenTable
    """"""
    TokenTransfer = TokenTransferTable
    """"""

    @classmethod
    def Aggregate(cls, expression: str, as_name: str):  # pylint: disable=invalid-name
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

    def _validate_columns(self, model_slug: str,
                          columns: List[str],
                          ledger_object_type: type[LedgerTable]):
        column_set = ledger_object_type.columns()

        for column in columns:
            if column.lower() not in column_set:
                raise InvalidColumnException(
                    model_slug,
                    column, list(column_set), "invalid column name")

    def _send_cwgo_query(self,  # pylint: disable=too-many-arguments
                         model_slug: str,
                         table_def: Type[LedgerTable],
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
        else:
            self._validate_columns(model_slug, columns, table_def)

        if where is None and limit is None and not aggregates:
            raise InvalidQueryException(
                model_slug,
                f'{model_slug} call must have a where or limit value for non-aggregate queries.')

        return self.context.run_model(model_slug,
                                      {'columns': columns,
                                       'aggregates': aggregates,
                                       'where': where,
                                       'groupBy': group_by,
                                       'having': having,
                                       'orderBy': order_by,
                                       'limit': limit,
                                       'offset': offset},
                                      return_type=LedgerModelOutput)

    @_query_method('Transaction')
    def get_transactions(self,  # pylint: disable=too-many-arguments
                         columns: Union[List[str], None] = None,
                         where: Union[str, None] = None,
                         group_by: Union[str, None] = None,
                         order_by: Union[str, None] = None,
                         limit: Union[str, None] = None,
                         offset: Union[str, None] = None,
                         aggregates: Union[List[LedgerAggregate], None] = None,
                         having: Union[str, None] = None) -> LedgerModelOutput:
        """
        Query data from the Transactions table.
        """
        return self._send_cwgo_query('ledger.transaction_data',
                                     TransactionTable,
                                     columns, where, group_by,
                                     order_by, limit, offset,
                                     aggregates, having)

    @_query_method('Trace')
    def get_traces(self,  # pylint: disable=too-many-arguments
                   columns: Union[List[str], None] = None,
                   where: Union[str, None] = None,
                   group_by: Union[str, None] = None,
                   order_by: Union[str, None] = None,
                   limit: Union[str, None] = None,
                   offset: Union[str, None] = None,
                   aggregates: Union[List[LedgerAggregate], None] = None,
                   having: Union[str, None] = None) -> LedgerModelOutput:
        """
        Query data from the Traces table.
        """
        return self._send_cwgo_query('ledger.trace_data',
                                     TraceTable,
                                     columns, where, group_by,
                                     order_by, limit, offset,
                                     aggregates, having)

    @_query_method('Log')
    def get_logs(self,  # pylint: disable=too-many-arguments
                 columns: Union[List[str], None] = None,
                 where: Union[str, None] = None,
                 group_by: Union[str, None] = None,
                 order_by: Union[str, None] = None,
                 limit: Union[str, None] = None,
                 offset: Union[str, None] = None,
                 aggregates: Union[List[LedgerAggregate], None] = None,
                 having: Union[str, None] = None) -> LedgerModelOutput:
        """
        Query data from the Logs table.
        """
        return self._send_cwgo_query('ledger.log_data',
                                     LogTable,
                                     columns, where, group_by,
                                     order_by, limit, offset,
                                     aggregates, having)

    @_query_method('Contract')
    def get_contracts(self,  # pylint: disable=too-many-arguments
                      columns: Union[List[str], None] = None,
                      where: Union[str, None] = None,
                      group_by: Union[str, None] = None,
                      order_by: Union[str, None] = None,
                      limit: Union[str, None] = None,
                      offset: Union[str, None] = None,
                      aggregates: Union[List[LedgerAggregate], None] = None,
                      having: Union[str, None] = None) -> LedgerModelOutput:
        """
        Query data from the Contracts table.
        """
        return self._send_cwgo_query('ledger.contract_data',
                                     ContractTable,
                                     columns, where, group_by,
                                     order_by, limit, offset,
                                     aggregates, having)

    @_query_method('Block')
    def get_blocks(self,  # pylint: disable=too-many-arguments
                   columns: Union[List[str], None] = None,
                   where: Union[str, None] = None,
                   group_by: Union[str, None] = None,
                   order_by: Union[str, None] = None,
                   limit: Union[str, None] = None,
                   offset: Union[str, None] = None,
                   aggregates: Union[List[LedgerAggregate], None] = None,
                   having: Union[str, None] = None) -> LedgerModelOutput:
        """
        Query data from the Blocks table.
        """
        return self._send_cwgo_query('ledger.block_data',
                                     BlockTable,
                                     columns, where, group_by,
                                     order_by, limit, offset,
                                     aggregates, having)

    @_query_method('Receipt')
    def get_receipts(self,  # pylint: disable=too-many-arguments
                     columns: Union[List[str], None] = None,
                     where: Union[str, None] = None,
                     group_by: Union[str, None] = None,
                     order_by: Union[str, None] = None,
                     limit: Union[str, None] = None,
                     offset: Union[str, None] = None,
                     aggregates: Union[List[LedgerAggregate], None] = None,
                     having: Union[str, None] = None) -> LedgerModelOutput:
        """
        Query data from the Receipts table.
        """
        return self._send_cwgo_query('ledger.receipt_data',
                                     ReceiptTable,
                                     columns, where, group_by,
                                     order_by, limit, offset,
                                     aggregates, having)

    @_query_method('Token')
    def get_erc20_tokens(self,  # pylint: disable=too-many-arguments
                         columns: Union[List[str], None] = None,
                         where: Union[str, None] = None,
                         group_by: Union[str, None] = None,
                         order_by: Union[str, None] = None,
                         limit: Union[str, None] = None,
                         offset: Union[str, None] = None,
                         aggregates: Union[List[LedgerAggregate], None] = None,
                         having: Union[str, None] = None) -> LedgerModelOutput:
        """
        Query data from the ERC20 Tokens table.
        """
        return self._send_cwgo_query('ledger.erc20_token_data',
                                     TokenTable,
                                     columns, where, group_by,
                                     order_by, limit, offset,
                                     aggregates, having)

    @_query_method('TokenTransfer')
    def get_erc20_transfers(self,  # pylint: disable=too-many-arguments
                            columns: Union[List[str], None] = None,
                            where: Union[str, None] = None,
                            group_by: Union[str, None] = None,
                            order_by: Union[str, None] = None,
                            limit: Union[str, None] = None,
                            offset: Union[str, None] = None,
                            aggregates: Union[List[LedgerAggregate], None] = None,
                            having: Union[str, None] = None) -> LedgerModelOutput:
        """
        Query data from the ERC20 Token Transfers table.
        """
        return self._send_cwgo_query('ledger.erc20_token_transfer_data',
                                     TokenTransferTable,
                                     columns, where, group_by,
                                     order_by, limit, offset,
                                     aggregates, having)
