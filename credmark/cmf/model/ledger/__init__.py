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


class Ledger:

    Transaction = TransactionTable
    Trace = TraceTable
    Block = BlockTable
    Contract = ContractTable
    Log = LogTable
    Receipt = ReceiptTable
    Token = TokenTable
    TokenTransfer = TokenTransferTable

    @classmethod
    def Aggregate(cls, expression: str, as_name: str):  # pylint: disable=invalid-name
        """
        Return a new LedgerAggregate instance that can be used in
        an aggregates list.

        For example::

            aggregates=[Ledger.Aggregate(f'SUM({Ledger.Block.Columns.GAS_USED})', 'total_gas')]
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

    def get_transactions(self,  # pylint: disable=too-many-arguments
                         columns: Union[List[str], None] = None,
                         where: Union[str, None] = None,
                         group_by: Union[str, None] = None,
                         order_by: Union[str, None] = None,
                         limit: Union[str, None] = None,
                         offset: Union[str, None] = None,
                         aggregates: Union[List[LedgerAggregate], None] = None,
                         having: Union[str, None] = None):
        """
        Query data from the Transactions table.
        """
        return self._send_cwgo_query('ledger.transaction_data',
                                     TransactionTable,
                                     columns, where, group_by,
                                     order_by, limit, offset,
                                     aggregates, having)

    def get_traces(self,  # pylint: disable=too-many-arguments
                   columns: Union[List[str], None] = None,
                   where: Union[str, None] = None,
                   group_by: Union[str, None] = None,
                   order_by: Union[str, None] = None,
                   limit: Union[str, None] = None,
                   offset: Union[str, None] = None,
                   aggregates: Union[List[LedgerAggregate], None] = None,
                   having: Union[str, None] = None):
        """
        Query data from the Traces table.
        """
        return self._send_cwgo_query('ledger.trace_data',
                                     TraceTable,
                                     columns, where, group_by,
                                     order_by, limit, offset,
                                     aggregates, having)

    def get_logs(self,  # pylint: disable=too-many-arguments
                 columns: Union[List[str], None] = None,
                 where: Union[str, None] = None,
                 group_by: Union[str, None] = None,
                 order_by: Union[str, None] = None,
                 limit: Union[str, None] = None,
                 offset: Union[str, None] = None,
                 aggregates: Union[List[LedgerAggregate], None] = None,
                 having: Union[str, None] = None):
        """
        Query data from the Logs table.
        """
        return self._send_cwgo_query('ledger.log_data',
                                     LogTable,
                                     columns, where, group_by,
                                     order_by, limit, offset,
                                     aggregates, having)

    def get_contracts(self,  # pylint: disable=too-many-arguments
                      columns: Union[List[str], None] = None,
                      where: Union[str, None] = None,
                      group_by: Union[str, None] = None,
                      order_by: Union[str, None] = None,
                      limit: Union[str, None] = None,
                      offset: Union[str, None] = None,
                      aggregates: Union[List[LedgerAggregate], None] = None,
                      having: Union[str, None] = None):
        """
        Query data from the Contracts table.
        """
        return self._send_cwgo_query('ledger.contract_data',
                                     ContractTable,
                                     columns, where, group_by,
                                     order_by, limit, offset,
                                     aggregates, having)

    def get_blocks(self,  # pylint: disable=too-many-arguments
                   columns: Union[List[str], None] = None,
                   where: Union[str, None] = None,
                   group_by: Union[str, None] = None,
                   order_by: Union[str, None] = None,
                   limit: Union[str, None] = None,
                   offset: Union[str, None] = None,
                   aggregates: Union[List[LedgerAggregate], None] = None,
                   having: Union[str, None] = None):
        """
        Query data from the Blocks table.
        """
        return self._send_cwgo_query('ledger.block_data',
                                     BlockTable,
                                     columns, where, group_by,
                                     order_by, limit, offset,
                                     aggregates, having)

    def get_receipts(self,  # pylint: disable=too-many-arguments
                     columns: Union[List[str], None] = None,
                     where: Union[str, None] = None,
                     group_by: Union[str, None] = None,
                     order_by: Union[str, None] = None,
                     limit: Union[str, None] = None,
                     offset: Union[str, None] = None,
                     aggregates: Union[List[LedgerAggregate], None] = None,
                     having: Union[str, None] = None):
        """
        Query data from the Receipts table.
        """
        return self._send_cwgo_query('ledger.receipt_data',
                                     ReceiptTable,
                                     columns, where, group_by,
                                     order_by, limit, offset,
                                     aggregates, having)

    def get_erc20_tokens(self,  # pylint: disable=too-many-arguments
                         columns: Union[List[str], None] = None,
                         where: Union[str, None] = None,
                         group_by: Union[str, None] = None,
                         order_by: Union[str, None] = None,
                         limit: Union[str, None] = None,
                         offset: Union[str, None] = None,
                         aggregates: Union[List[LedgerAggregate], None] = None,
                         having: Union[str, None] = None):
        """
        Query data from the ERC20 Tokens table.
        """
        return self._send_cwgo_query('ledger.erc20_token_data',
                                     TokenTable,
                                     columns, where, group_by,
                                     order_by, limit, offset,
                                     aggregates, having)

    def get_erc20_transfers(self,  # pylint: disable=too-many-arguments
                            columns: Union[List[str], None] = None,
                            where: Union[str, None] = None,
                            group_by: Union[str, None] = None,
                            order_by: Union[str, None] = None,
                            limit: Union[str, None] = None,
                            offset: Union[str, None] = None,
                            aggregates: Union[List[LedgerAggregate], None] = None,
                            having: Union[str, None] = None):
        """
        Query data from the ERC20 Token Transfers table.
        """
        return self._send_cwgo_query('ledger.erc20_token_transfer_data',
                                     TokenTransferTable,
                                     columns, where, group_by,
                                     order_by, limit, offset,
                                     aggregates, having)
