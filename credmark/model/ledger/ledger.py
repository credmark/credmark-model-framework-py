from typing import Type, Union, List
from ...types.models.ledger import LedgerModelOutput
from ... import model

from .errors import InvalidColumnException, InvalidQueryException
from .tables import BlockTable, ContractTable, \
    LogTable, ReceiptTable, TokenTable, TokenTransferTable, \
    TraceTable, TransactionTable, LedgerTable


class Ledger:

    Transaction = TransactionTable
    Trace = TraceTable
    Block = BlockTable
    Contract = ContractTable
    Log = LogTable
    Receipt = ReceiptTable
    Token = TokenTable
    TokenTransfer = TokenTransferTable

    def __init__(self, context):
        # We type the property here to avoid circular ref
        self.context: model.ModelContext = context

    def _validate_columns(self, model_slug: str,
                          columns: List[str],
                          ledger_object_type: type[LedgerTable]):
        column_set = ledger_object_type.columns()

        for column in columns:
            if column.lower() not in column_set:
                raise InvalidColumnException(
                    model_slug,
                    column, list(column_set), "invalid column name")

    def _send_cwgo_query(self,
                         model_slug: str,
                         table_def: Type[LedgerTable],
                         columns: List[str],
                         where: Union[str, None] = None,
                         group_by: Union[str, None] = None,
                         order_by: Union[str, None] = None,
                         limit: Union[str, None] = None,
                         offset: Union[str, None] = None):
        self._validate_columns(model_slug, columns, table_def)

        if where is None and limit is None:
            raise InvalidQueryException(
                model_slug, f'{model_slug} call must have a where or limit value set.')

        return self.context.run_model(model_slug,
                                      {'columns': columns,
                                       'where': where,
                                       'groupBy': group_by,
                                       'orderBy': order_by,
                                       'limit': limit,
                                       'offset': offset},
                                      return_type=LedgerModelOutput)

    def get_transactions(self, columns: List[str],
                         where: Union[str, None] = None,
                         group_by: Union[str, None] = None,
                         order_by: Union[str, None] = None,
                         limit: Union[str, None] = None,
                         offset: Union[str, None] = None):
        return self._send_cwgo_query('ledger.transaction_data',
                                     TransactionTable,
                                     columns, where, group_by,
                                     order_by, limit, offset)

    def get_traces(self, columns: List[str],
                   where: Union[str, None] = None,
                   group_by: Union[str, None] = None,
                   order_by: Union[str, None] = None,
                   limit: Union[str, None] = None,
                   offset: Union[str, None] = None):
        return self._send_cwgo_query('ledger.trace_data',
                                     TraceTable,
                                     columns, where, group_by,
                                     order_by, limit, offset)

    def get_logs(self, columns: List[str],
                 where: Union[str, None] = None,
                 group_by: Union[str, None] = None,
                 order_by: Union[str, None] = None,
                 limit: Union[str, None] = None,
                 offset: Union[str, None] = None):
        return self._send_cwgo_query('ledger.log_data',
                                     LogTable,
                                     columns, where, group_by,
                                     order_by, limit, offset)

    def get_contracts(self, columns: List[str],
                      where: Union[str, None] = None,
                      group_by: Union[str, None] = None,
                      order_by: Union[str, None] = None,
                      limit: Union[str, None] = None,
                      offset: Union[str, None] = None):
        return self._send_cwgo_query('ledger.contract_data',
                                     ContractTable,
                                     columns, where, group_by,
                                     order_by, limit, offset)

    def get_blocks(self, columns: List[str],
                   where: Union[str, None] = None,
                   group_by: Union[str, None] = None,
                   order_by: Union[str, None] = None,
                   limit: Union[str, None] = None,
                   offset: Union[str, None] = None):
        return self._send_cwgo_query('ledger.block_data',
                                     BlockTable,
                                     columns, where, group_by,
                                     order_by, limit, offset)

    def get_receipts(self, columns: List[str],
                     where: Union[str, None] = None,
                     group_by: Union[str, None] = None,
                     order_by: Union[str, None] = None,
                     limit: Union[str, None] = None,
                     offset: Union[str, None] = None):
        return self._send_cwgo_query('ledger.receipt_data',
                                     ReceiptTable,
                                     columns, where, group_by,
                                     order_by, limit, offset)

    def get_erc20_tokens(self, columns: List[str],
                         where: Union[str, None] = None,
                         group_by: Union[str, None] = None,
                         order_by: Union[str, None] = None,
                         limit: Union[str, None] = None,
                         offset: Union[str, None] = None):
        return self._send_cwgo_query('ledger.erc20_token_data',
                                     TokenTable,
                                     columns, where, group_by,
                                     order_by, limit, offset)

    def get_erc20_transfers(self, columns: List[str],
                            where: Union[str, None] = None,
                            group_by: Union[str, None] = None,
                            order_by: Union[str, None] = None,
                            limit: Union[str, None] = None,
                            offset: Union[str, None] = None):
        return self._send_cwgo_query('ledger.erc20_token_transfer_data',
                                     TokenTransferTable,
                                     columns, where, group_by,
                                     order_by, limit, offset)
