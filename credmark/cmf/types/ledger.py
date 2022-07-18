import inspect
from typing import Dict, List

import pandas as pd
from credmark.cmf.model.errors import ModelRunError
from credmark.dto import DTO, DTOField, IterableListGenericDTO, PrivateAttr

from .ledger_errors import InvalidColumnException


class LedgerAggregate(DTO):
    """
    An aggregate column in a query.
    It is defined by an expression and the name to use as the
    column name in the returned data.
    """
    expression: str = DTOField(..., description='Aggregate expression, for example "MAX(GAS_USED)"')
    asName: str = DTOField(..., description='Returned as data column name')


class LedgerModelOutput(IterableListGenericDTO[dict]):
    """
    The return value for a ledger query.
    """
    data: List[dict] = DTOField(
        default=[], description='A list of dicts which are the rows of data')

    _iterator: str = PrivateAttr('data')

    def to_dataframe(self):
        return pd.DataFrame(self.data)


class ColumnField(str):
    # pylint:disable=invalid-name, too-many-public-methods
    def str(self):
        return str(self)

    def squote_and_lower(self):
        return ColumnField(f"'{self.lower()}'")

    def squote(self):
        return ColumnField(f"'{self}'")

    def dquote(self):
        return ColumnField(f'"{self}"')

    def desc(self):
        return ColumnField(self + ' desc')

    def asc(self):
        return ColumnField(self + ' asc')

    def _compare(self, value, force, op):
        if isinstance(value, str):
            if force:
                return ColumnField(f'{self} {op} {ColumnField(value).squote()}')
            else:
                return ColumnField(f'{self} {op} {ColumnField(value).squote_and_lower()}')

        return ColumnField(f'{self} {op} {value}')

    def eq(self, value, force=False):
        return self._compare(value, force, '=')

    def gt(self, value, force=False):
        return self._compare(value, force, '>')

    def ge(self, value, force=False):
        return self._compare(value, force, '>=')

    def lt(self, value, force=False):
        return self._compare(value, force, '<')

    def le(self, value, force=False):
        return self._compare(value, force, '<=')

    def _list_of_fields(self, values, force):
        if len(values) == 0:
            raise ModelRunError(f'column {self} is not in empty set {values}')

        if isinstance(values[0], str):
            if force:
                list_of_fields = ",".join([ColumnField(v).squote() for v in values])
            else:
                list_of_fields = ",".join([ColumnField(v).squote_and_lower() for v in values])
        else:
            list_of_fields = ",".join([str(v) for v in values])
        return list_of_fields

    def in_(self, values, force=False):
        list_of_fields = self._list_of_fields(values, force)
        return ColumnField(f'{self} in ({list_of_fields})')

    def not_in_(self, values, force=False):
        list_of_fields = self._list_of_fields(values, force)
        return ColumnField(f'{self} not in ({list_of_fields})')

    def _two_fields(self, value1, value2, force):
        if not isinstance(value1, type(value2)) and not isinstance(value2, type(value1)):
            raise ModelRunError(
                f'{value1} and {value2} shall be of the same type for [not] between')

        if isinstance(value1, str):
            if force:
                return (ColumnField(value1).squote(),
                        ColumnField(value2).squote())
            else:
                return (ColumnField(value1).squote_and_lower(),
                        ColumnField(value2).squote_and_lower())
        return value1, value2

    def between_(self, value1, value2, force=False):
        f1, f2 = self._two_fields(value1, value2, force)
        return ColumnField(f'{self} between {f1} and {f2}')

    def not_between_(self, value1, value2, force=False):
        f1, f2 = self._two_fields(value1, value2, force)
        return ColumnField(f'{self} not between {f1} and {f2}')

    def and_(self, value):
        return ColumnField(self + ' and ' + value)

    def or_(self, value):
        return ColumnField(self + ' or ' + value)

    def parentheses_(self):
        return ColumnField('(' + self + ')')

    def comma_(self, value):
        return ColumnField(self + ', ' + value)

    def func_(self, func_name):
        return ColumnField(f'{func_name}({self})')

    def sum_(self):
        return self.func_('SUM')

    def max_(self):
        return self.func_('MAX')

    def min_(self):
        return self.func_('MIN')

    def avg_(self):
        return self.func_('AVG')

    def neg_(self):
        return '-' + self


class LedgerTable:
    """
    Base class for ledger data tables

    A mixin class with LedgerQuery to create class LedgerQuery{Table}
    """

    # Use a doc string """""" after each property so they will be
    # documented automatically.

    _column_dict: Dict[str, ColumnField] = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._column_dict = {}
        for i in inspect.getmembers(self.__class__):
            if isinstance(getattr(self.__class__, i[0]), ColumnField) and i[0][0].isalpha():
                self._column_dict[i[0]] = i[1]

        for i in kwargs['more_cols']:
            self._column_dict[i[0]] = ColumnField(i[1])
            setattr(self, i[0], ColumnField(i[1]))

    def __dir__(self):
        return list(super().__dir__())

    def __repr__(self):
        return str(dir(self))

    def __getitem__(self, name):
        return self._column_dict[name]

    def __getattr__(self, name):
        if name in self._column_dict:
            return self._column_dict[name]
        raise AttributeError(name)

    @property
    def columns(self) -> List[str]:
        """
        Return the set of column names for the table.
        They will be used in the database.

        For contract ledger tables, the set will include
        all contract-specific columns.
        """
        return list(self._column_dict.values())

    @property
    def colnames(self) -> List[str]:
        """
        Return the set of column names in the table.
        They can be used in the query.
        """
        return list(self._column_dict.keys())

    def _validate_columns(self, model_slug: str,
                          columns: List[str]):

        column_set = set(self.columns)
        for column in columns:
            if column not in column_set:
                raise InvalidColumnException(
                    model_slug,
                    column, list(column_set), "invalid column name")


class TransactionTable(LedgerTable):
    """
    Transactions ledger data table
    Column names
    """

    HASH = ColumnField('hash')
    """"""
    NONCE = ColumnField('nonce')
    """"""
    BLOCK_HASH = ColumnField('block_hash')
    """"""
    TRANSACTION_INDEX = ColumnField('transaction_index')
    """"""
    FROM_ADDRESS = ColumnField('from_address')
    """"""
    TO_ADDRESS = ColumnField('to_address')
    """"""
    VALUE = ColumnField('value')
    """"""
    GAS = ColumnField('gas')
    """"""
    GAS_PRICE = ColumnField('gas_price')
    """"""
    INPUT = ColumnField('input')
    """"""
    BLOCK_TIMESTAMP = ColumnField('block_timestamp')
    """"""
    MAX_FEE_PER_GAS = ColumnField('max_fee_per_gas')
    """"""
    MAX_PRIORITY_FEE_PER_GAS = ColumnField('max_priority_fee_per_gas')
    """"""
    TRANSACTION_TYPE = ColumnField('transaction_type')
    """"""
    BLOCK_NUMBER = ColumnField('block_number')
    """"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class TraceTable(LedgerTable):
    """
    Trace ledger data table
    Column names
    """

    BLOCK_NUMBER = ColumnField('block_number')
    """"""
    TRANSACTION_HASH = ColumnField('transaction_hash')
    """"""
    TRANSACTION_INDEX = ColumnField('transaction_index')
    """"""
    FROM_ADDRESS = ColumnField('from_address')
    """"""
    TO_ADDRESS = ColumnField('to_address')
    """"""
    VALUE = ColumnField('value')
    """"""
    INPUT = ColumnField('input')
    """"""
    OUTPUT = ColumnField('output')
    """"""
    TRACE_TYPE = ColumnField('trace_type')
    """"""
    CALL_TYPE = ColumnField('call_type')
    """"""
    REWARD_TYPE = ColumnField('reward_type')
    """"""
    GAS = ColumnField('gas')
    """"""
    GAS_USED = ColumnField('gas_used')
    """"""
    SUB_TRACES = ColumnField('sub_traces')
    """"""
    TRACE_ADDRESS = ColumnField('trace_address')
    """"""
    ERROR = ColumnField('error')
    """"""
    STATUS = ColumnField('status')
    """"""
    TRACE_ID = ColumnField('trace_id')
    """"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class BlockTable(LedgerTable):
    """
    Blocks ledger data table
    Column names
    """

    NUMBER = ColumnField('number')
    """"""
    HASH = ColumnField('hash')
    """"""
    PARENT_HASH = ColumnField('parent_hash')
    """"""
    NONCE = ColumnField('nonce')
    """"""
    SHA3_UNCLES = ColumnField('sha3_uncles')
    """"""
    LOGS_BLOOM = ColumnField('logs_bloom')
    """"""
    TRANSACTIONS_ROOT = ColumnField('transactions_root')
    """"""
    STATE_ROOT = ColumnField('state_root')
    """"""
    RECEIPTS_ROOT = ColumnField('receipts_root')
    """"""
    MINER = ColumnField('miner')
    """"""
    DIFFICULTY = ColumnField('difficulty')
    """"""
    TOTAL_DIFFICULTY = ColumnField('total_difficulty')
    """"""
    SIZE = ColumnField('size')
    """"""
    EXTRA_DATA = ColumnField('extra_data')
    """"""
    GAS_LIMIT = ColumnField('gas_limit')
    """"""
    GAS_USED = ColumnField('gas_used')
    """"""
    TIMESTAMP = ColumnField('timestamp')
    """"""
    TS = ColumnField('ts')
    """"""
    TRANSACTION_COUNT = ColumnField('transaction_count')
    """"""
    BASE_FEE_PER_GAS = ColumnField('base_fee_per_gas')
    """"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ContractTable(LedgerTable):
    """
    Contracts ledger data table
    Column names
    """

    ADDRESS = ColumnField('address')
    """"""
    BYTECODE = ColumnField('bytecode')
    """"""
    FUNCTION_SIGHASHES = ColumnField('function_sighashes')
    """"""
    IS_ERC20 = ColumnField('is_erc20 ')
    """"""
    IS_ERC721 = ColumnField('is_erc721 ')
    """"""
    BLOCK_NUMBER = ColumnField('block_number')
    """"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class LogTable(LedgerTable):
    """
    Logs ledger data table
    Column names
    """

    LOG_INDEX = ColumnField('log_index')
    """"""
    TRANSACTION_HASH = ColumnField('transaction_hash')
    """"""
    TRANSACTION_INDEX = ColumnField('transaction_index')
    """"""
    BLOCK_HASH = ColumnField('block_hash')
    """"""
    BLOCK_NUMBER = ColumnField('block_number')
    """"""
    ADDRESS = ColumnField('address')
    """"""
    DATA = ColumnField('data')
    """"""
    TOPICS = ColumnField('topics')
    """"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ReceiptTable(LedgerTable):
    """
    Receipts ledger data table
    Column names
    """

    TRANSACTION_HASH = ColumnField('transaction_hash')
    """"""
    TRANSACTION_INDEX = ColumnField('transaction_index')
    """"""
    BLOCK_HASH = ColumnField('block_hash')
    """"""
    BLOCK_NUMBER = ColumnField('block_number')
    """"""
    CUMULATIVE_GAS_USED = ColumnField('cumulative_gas_used')
    """"""
    GAS_USED = ColumnField('gas_used')
    """"""
    CONTRACT_ADDRESS = ColumnField('contract_address')
    """"""
    ROOT = ColumnField('root')
    """"""
    STATUS = ColumnField('status')
    """"""
    EFFECTIVE_GAS_PRICE = ColumnField('effective_gas_price')
    """"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class TokenTable(LedgerTable):
    """
    Tokens ledger data table
    Column names
    """

    ADDRESS = ColumnField('address')
    """"""
    SYMBOL = ColumnField('symbol')
    """"""
    NAME = ColumnField('name')
    """"""
    DECIMALS = ColumnField('decimals')
    """"""
    TOTAL_SUPPLY = ColumnField('total_supply')
    """"""
    BLOCK_NUMBER = ColumnField('block_number')
    """"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class TokenTransferTable(LedgerTable):
    """
    Token transfers ledger data table
    Column names
    """

    TOKEN_ADDRESS = ColumnField('token_address')
    """"""
    FROM_ADDRESS = ColumnField('from_address')
    """"""
    TO_ADDRESS = ColumnField('to_address')
    """"""
    VALUE = ColumnField('value')
    """"""
    TRANSACTION_HASH = ColumnField('transaction_hash')
    """"""
    LOG_INDEX = ColumnField('log_index')
    """"""
    BLOCK_NUMBER = ColumnField('block_number')
    """"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class TokenBalanceTable(LedgerTable):
    """
    Token balance ledger data table
    Column names
    """

    BLOCK_TIMESTAMP = ColumnField('block_timestamp')
    """"""
    BLOCK_HASH = ColumnField('block_hash')
    """"""
    BLOCK_NUMBER = ColumnField('block_number')
    """"""
    TOKEN_ADDRESS = ColumnField('token_address')
    """"""
    TRANSACTION_HASH = ColumnField('transaction_hash')
    """"""
    LOG_INDEX = ColumnField('log_index')
    """"""
    ADDRESS = ColumnField('address')
    """"""
    FROM_ADDRESS = ColumnField('from_address')
    """"""
    TO_ADDRESS = ColumnField('to_address')
    """"""
    TRANSACTION_VALUE = ColumnField('transaction_value')
    """"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
