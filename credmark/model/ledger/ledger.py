from typing import Union, List
from .errors import InvalidColumnException
from .definitions import TransactionDefinition, LedgerObject
from .query import LedgerQuery


class Ledger:
    def __init__(self, context):
        self.context = context
        # TODO: Do we need these instance vars?
        self.columns = None
        self.query = None

    def _validate_columns(self, columns: List[str], ledger_object_type: type[LedgerObject]):
        for column in columns:
            if column not in ledger_object_type.columns:
                raise InvalidColumnException(
                    column, ledger_object_type.columns, "invalid column name")

    def get_transactions(self, columns: List[str], query: Union[LedgerQuery, None]):
        self._validate_columns(columns, TransactionDefinition)
        self.query = query
        self.columns = columns
        return self.context.run_model('ledger.transaction_data', {'columns': columns, 'query': query})

    def get_traces(self, columns: List[str], query: Union[LedgerQuery, None]):
        self.query = query
        self.columns = columns
        return self.context.run_model('ledger.trace_data', {'columns': columns, 'query': query})

    def get_logs(self, columns: List[str], query: Union[LedgerQuery, None]):
        self.query = query
        self.columns = columns
        return self.context.run_model('ledger.log_data', {'columns': columns, 'query': query})

    def get_contracts(self, columns: List[str], query: Union[LedgerQuery, None]):
        self.query = query
        self.columns = columns
        return self.context.run_model('ledger.contract_data', {'columns': columns, 'query': query})

    def get_blocks(self, columns: List[str], query: Union[LedgerQuery, None]):
        self.query = query
        self.columns = columns
        return self.context.run_model('ledger.block_data', {'columns': columns, 'query': query})

    def get_receipts(self, columns: List[str], query: Union[LedgerQuery, None]):
        self.query = query
        self.columns = columns
        return self.context.run_model('ledger.receipt_data', {'columns': columns, 'query': query})

    def get_erc20_transfers(self, columns: List[str], query: Union[LedgerQuery, None]):
        self.query = query
        self.columns = columns
        return self.context.run_model('ledger.erc20_transfer_data',
                                      {'columns': columns, 'query': query})
