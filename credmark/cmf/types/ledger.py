# ruff: noqa: E722

import inspect
from datetime import datetime
from enum import Enum
from typing import Dict, List, Tuple, Union

import pandas as pd

from credmark.cmf.model.errors import ModelRunError
from credmark.dto import DTO, DTOField, IterableListGenericDTO, PrivateAttr

from .ledger_errors import InvalidColumnException


class JoinType(str, Enum):
    INNER = "inner"
    LEFT_OUTER = "leftOuter"
    RIGHT_OUTER = "rightOuter"
    FULL_OUTER = "fullOuter"
    CROSS = "cross"
    NATURAL = "natural"


class LedgerAggregate(DTO):
    """
    An aggregate column in a query.
    It is defined by an expression and the name to use as the
    column name in the returned data.
    """

    expression: str = DTOField(..., description='Aggregate expression, for example "MAX(GAS_USED)"')
    asName: str = DTOField(..., description="Returned as data column name")


class LedgerJoin(DTO):
    """
    Join in a query.
    It is defined by table key, table alias and
    expression to join on.
    """

    type: Union[JoinType, None] = DTOField(description="Type of join. Defaults to inner join.")
    tableKey: str = DTOField(..., description="Key of the table to be joined")
    alias: Union[str, None] = DTOField(description="Alias for the table")
    on: str = DTOField(..., description='Join expression, for example "a.address = b.address"')


class LedgerModelOutput(IterableListGenericDTO[dict]):
    """
    The return value for a ledger query.

    _bigint_cols stores the list of columns of big integer.
    They are extracted as character from DB and converted back to int in .to_dataframe().
    """

    data: List[dict] = DTOField(
        default=[], description="A list of dicts which are the rows of data"
    )

    _iterator: str = PrivateAttr("data")

    _bigint_cols: List[str] = PrivateAttr([])

    def to_dataframe(self):
        df = pd.DataFrame(self.data)
        if df.shape[0] > 0:
            for c in self._bigint_cols:
                if c in df.columns:
                    col_type = df[c].dtype
                    if col_type == "float64":
                        df = df.assign(**{c: (lambda x, c=c: x[c].apply(round))})
                    elif col_type in ["int64", "uint64"]:
                        pass
                    elif col_type == "O":
                        try:
                            df = df.astype({c: int})
                        except:  # pylint:disable=bare-except
                            try:
                                df = df.astype({c: "Int64"})
                            except ValueError:
                                pass
                            except OverflowError:
                                df = df.assign(**{c: (lambda x, c=c: x[c].apply(int))})
                    else:
                        raise TypeError(f"column {c} has unsupported column type {col_type}")
        return df

    def bigint_cols(self):
        return self._bigint_cols

    def set_bigint_cols(self, cols):
        self._bigint_cols = cols


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
        return ColumnField(self + " desc")

    def asc(self):
        return ColumnField(self + " asc")

    def _maybe_quote_and_lower(self, value, case_sensitive=False):
        """
        case_sensitive: If the value is not case sensitive, it will be converted to lower case.
        This takes care of addresses which are stored in lower case all across the database.

        By default values are considered case insensitive
        """
        # Don't add quotes when the value is a column
        if isinstance(value, ColumnField):
            return ColumnField(value if case_sensitive else value.lower())

        if isinstance(value, str):
            col_field = ColumnField(value)
            return ColumnField(
                col_field.squote() if case_sensitive else col_field.squote_and_lower()
            )

        return value

    def _compare(self, value, case_sensitive, op):
        return ColumnField(f"{self} {op} {self._maybe_quote_and_lower(value, case_sensitive)}")

    def eq(self, value, case_sensitive=False):
        return self._compare(value, case_sensitive, "=")

    def ne(self, value, case_sensitive=False):
        return self._compare(value, case_sensitive, "!=")

    def gt(self, value, case_sensitive=False):
        return self._compare(value, case_sensitive, ">")

    def ge(self, value, case_sensitive=False):
        return self._compare(value, case_sensitive, ">=")

    def lt(self, value, case_sensitive=False):
        return self._compare(value, case_sensitive, "<")

    def le(self, value, case_sensitive=False):
        return self._compare(value, case_sensitive, "<=")

    def _list_of_fields(self, values, case_sensitive):
        if len(values) == 0:
            raise ModelRunError(f"column {self} is not in empty set {values}")

        return ",".join([str(self._maybe_quote_and_lower(v, case_sensitive)) for v in values])

    def in_(self, values, case_sensitive=False):
        list_of_fields = self._list_of_fields(values, case_sensitive)
        return ColumnField(f"{self} in ({list_of_fields})")

    def not_in_(self, values, case_sensitive=False):
        list_of_fields = self._list_of_fields(values, case_sensitive)
        return ColumnField(f"{self} not in ({list_of_fields})")

    def between_(self, value1, value2, case_sensitive=False):
        f1 = self._maybe_quote_and_lower(value1, case_sensitive)
        f2 = self._maybe_quote_and_lower(value2, case_sensitive)
        return ColumnField(f"{self} between {f1} and {f2}")

    def not_between_(self, value1, value2, case_sensitive=False):
        f1 = self._maybe_quote_and_lower(value1, case_sensitive)
        f2 = self._maybe_quote_and_lower(value2, case_sensitive)
        return ColumnField(f"{self} not between {f1} and {f2}")

    def and_(self, value):
        return ColumnField(f"{self} and {value}")

    def or_(self, value):
        return ColumnField(f"{self} or {value}")

    def parentheses_(self):
        return ColumnField(f"({self})")

    def comma_(self, value):
        return ColumnField(f"{self}, {value}")

    def func_(self, func_name):
        return ColumnField(f"{func_name}({self})")

    def sum_(self):
        return self.func_("SUM")

    def count_(self):
        return self.func_("COUNT")

    def distinct(self):
        return ColumnField(f"DISTINCT {self}")

    def count_distinct_(self):
        return self.distinct().func_("COUNT")

    def max_(self):
        return self.func_("MAX")

    def min_(self):
        return self.func_("MIN")

    def avg_(self):
        return self.func_("AVG")

    def neg_(self):
        return "-" + self

    def op_(self, col, op):
        return ColumnField(f"{self} {op} {col}").parentheses_()

    def plus_(self, col):
        return self.op_(col, "+")

    def minus_(self, col):
        return self.op_(col, "-")

    def mul_(self, col):
        return self.op_(col, "*")

    def div_(self, col):
        return self.op_(col, "/")

    def as_text(self):
        return ColumnField(f"{self}::TEXT")

    def as_bigint(self):
        return ColumnField(f"{self}::BIGINT")

    def as_integer(self):
        return ColumnField(f"{self}::INTEGER")

    def as_numeric(self):
        return ColumnField(f"{self}::NUMERIC")

    def is_null(self):
        return ColumnField(f"{self} is null")

    def is_not_null(self):
        return ColumnField(f"{self} is not null")

    def extract_epoch(self):
        return ColumnField(f"extract(epoch from {self})")

    def to_timestamp(self):
        return ColumnField(f"to_timestamp({self})")

    @staticmethod
    def from_iso8601_str(timestamp):
        if timestamp.endswith("Z"):
            timestamp = timestamp[:-1] + "+00:00"
        return int(datetime.fromisoformat(timestamp).timestamp())


class LedgerTable:
    """
    Base class for ledger data tables

    A mixin class with LedgerQuery to create class LedgerQuery{Table}
    """

    # Use a doc string """""" after each property so they will be
    # documented automatically.

    _table_key: str
    _alias: Union[str, None] = None
    _more_cols: Union[List[Tuple[str, str]], None]
    _column_dict: Dict[str, ColumnField] = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._table_key = kwargs["table_key"]
        self._more_cols = kwargs["more_cols"]

        self._column_dict = {}
        for i in inspect.getmembers(self.__class__):
            if isinstance(getattr(self.__class__, i[0]), ColumnField) and i[0][0].isalpha():
                self._column_dict[i[0]] = i[1]

        for i in self._more_cols or []:
            self._column_dict[i[0]] = ColumnField(i[1])
            setattr(self, i[0], ColumnField(i[1]))

    def __dir__(self):
        return list(super().__dir__())

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, self.columns)

    def __getitem__(self, name):
        return self._column_dict[name]

    def __getattr__(self, name):
        if name in self._column_dict:
            return self._column_dict[name]
        raise AttributeError(f"{name} not found in {self.colnames}")

    def as_(self, alias: str):
        self._alias = alias
        self._column_dict = {}
        for i in inspect.getmembers(self.__class__):
            if isinstance(getattr(self.__class__, i[0]), ColumnField) and i[0][0].isalpha():
                field = ColumnField(f"{self._alias}.{i[1]}")
                setattr(self, i[0], field)
                self._column_dict[i[0]] = field

        for i in self._more_cols or []:
            field = ColumnField(f"{self._alias}.{i[1]}")
            self._column_dict[i[0]] = field
            setattr(self, i[0], field)

        return self

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

    def _validate_columns(self, model_slug: str, columns: List[str]):
        column_set = set(self.columns)
        for column in columns:
            if column not in column_set:
                raise InvalidColumnException(
                    model_slug,
                    column,
                    list(column_set),
                    f"invalid column name '{column}' not found in {list(column_set)}",
                )

    def describe(self) -> list[tuple[str, str]]:
        return [(k, self.TYPE_MAPPER[k]) for k in self.columns]  # type: ignore

    @property
    def alias(self):
        return self._alias

    @property
    def table_key(self):
        return self._table_key

    @property
    def bigint_cols(self):
        return []


class BlockTable(LedgerTable):
    """
    Blocks ledger data table
    Column names
    """

    NUMBER = ColumnField("number")
    """"""
    HASH = ColumnField("hash")
    """"""
    PARENT_HASH = ColumnField("parent_hash")
    """"""
    NONCE = ColumnField("nonce")
    """"""
    SHA3_UNCLES = ColumnField("sha3_uncles")
    """"""
    LOGS_BLOOM = ColumnField("logs_bloom")
    """"""
    TRANSACTIONS_ROOT = ColumnField("transactions_root")
    """"""
    STATE_ROOT = ColumnField("state_root")
    """"""
    RECEIPTS_ROOT = ColumnField("receipts_root")
    """"""
    MINER = ColumnField("miner")
    """"""
    DIFFICULTY = ColumnField("difficulty")
    """"""
    TOTAL_DIFFICULTY = ColumnField("total_difficulty")
    """"""
    SIZE = ColumnField("size")
    """"""
    EXTRA_DATA = ColumnField("extra_data")
    """"""
    GAS_LIMIT = ColumnField("gas_limit")
    """"""
    GAS_USED = ColumnField("gas_used")
    """"""
    TIMESTAMP = ColumnField("timestamp")
    """"""
    TRANSACTION_COUNT = ColumnField("transaction_count")
    """"""
    BASE_FEE_PER_GAS = ColumnField("base_fee_per_gas")
    """"""

    TYPE_MAPPER = {
        "number": "int",
        "hash": "str",
        "parent_hash": "str",
        "nonce": "str",
        "sha3_uncles": "str",
        "logs_bloom": "str",
        "transactions_root": "str",
        "state_root": "str",
        "receipts_root": "str",
        "miner": "str",
        "difficulty": "int",
        "total_difficulty": "int",
        "size": "int",
        "extra_data": "str",
        "gas_limit": "int",
        "gas_used": "int",
        "timestamp": "str",
        "transaction_count": "int",
        "base_fee_per_gas": "int",
    }

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    @property
    def bigint_cols(self) -> List[ColumnField]:
        return [self.DIFFICULTY, self.TOTAL_DIFFICULTY]


class ContractTable(LedgerTable):
    """
    Contracts ledger data table
    Column names
    """

    ADDRESS = ColumnField("address")
    """"""
    BYTECODE = ColumnField("bytecode")
    """"""
    # FUNCTION_SIGHASHES = ColumnField('function_sighashes')
    # """"""
    IS_ERC20 = ColumnField("is_erc20")
    """"""
    IS_ERC721 = ColumnField("is_erc721")
    """"""
    BLOCK_HASH = ColumnField("block_hash")
    """"""
    BLOCK_NUMBER = ColumnField("block_number")
    """"""
    BLOCK_TIMESTAMP = ColumnField("block_timestamp")
    """"""

    TYPE_MAPPER = {
        "address": "str",
        "bytecode": "str",
        "function_sighashes": "str",
        "is_erc20": "bool",
        "is_erc721": "bool",
        "block_hash": "str",
        "block_number": "int",
        "block_timestamp": "str",
    }

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    @property
    def bigint_cols(self) -> List[ColumnField]:
        return []


class LogTable(LedgerTable):
    """
    Logs ledger data table
    Column names
    """

    LOG_INDEX = ColumnField("log_index")
    """"""
    TRANSACTION_HASH = ColumnField("transaction_hash")
    """"""
    TRANSACTION_INDEX = ColumnField("transaction_index")
    """"""
    BLOCK_HASH = ColumnField("block_hash")
    """"""
    BLOCK_NUMBER = ColumnField("block_number")
    """"""
    BLOCK_TIMESTAMP = ColumnField("block_timestamp")
    """"""
    ADDRESS = ColumnField("address")
    """"""
    DATA = ColumnField("data")
    """"""
    TOPIC0 = ColumnField("topic0")
    """"""
    TOPIC1 = ColumnField("topic1")
    """"""
    TOPIC2 = ColumnField("topic2")
    """"""
    TOPIC3 = ColumnField("topic3")
    """"""

    TYPE_MAPPER = {
        "log_index": "int",
        "transaction_hash": "str",
        "transaction_index": "int",
        "block_hash": "str",
        "block_number": "int",
        "block_timestamp": "str",
        "address": "str",
        "data": "str",
        "topic0": "str",
        "topic1": "str",
        "topic2": "str",
        "topic3": "str",
    }

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    @property
    def bigint_cols(self) -> List[ColumnField]:
        return []


class ReceiptTable(LedgerTable):
    """
    Receipts ledger data table
    Column names
    """

    TRANSACTION_HASH = ColumnField("transaction_hash")
    """"""
    TRANSACTION_INDEX = ColumnField("transaction_index")
    """"""
    BLOCK_HASH = ColumnField("block_hash")
    """"""
    BLOCK_NUMBER = ColumnField("block_number")
    """"""
    BLOCK_TIMESTAMP = ColumnField("block_timestamp")
    """"""
    CUMULATIVE_GAS_USED = ColumnField("cumulative_gas_used")
    """"""
    GAS_USED = ColumnField("gas_used")
    """"""
    CONTRACT_ADDRESS = ColumnField("contract_address")
    """"""
    ROOT = ColumnField("root")
    """"""
    STATUS = ColumnField("status")
    """"""
    EFFECTIVE_GAS_PRICE = ColumnField("effective_gas_price")
    """"""

    TYPE_MAPPER = {
        "transaction_hash": "str",
        "transaction_index": "int",
        "block_hash": "str",
        "block_number": "int",
        "block_timestamp": "str",
        "cumulative_gas_used": "int",
        "gas_used": "int",
        "contract_address": "Optional[str]",
        "root": "Optional[str]",
        "status": "int",
        "effective_gas_price": "int",
    }

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    @property
    def bigint_cols(self) -> List[ColumnField]:
        return [self.CUMULATIVE_GAS_USED, self.GAS_USED, self.EFFECTIVE_GAS_PRICE]


class TransactionTable(LedgerTable):
    """
    Transactions ledger data table
    Column names
    """

    HASH = ColumnField("hash")
    """"""
    NONCE = ColumnField("nonce")
    """"""
    BLOCK_HASH = ColumnField("block_hash")
    """"""
    TRANSACTION_INDEX = ColumnField("transaction_index")
    """"""
    FROM_ADDRESS = ColumnField("from_address")
    """"""
    TO_ADDRESS = ColumnField("to_address")
    """"""
    VALUE = ColumnField("value")
    """"""
    GAS = ColumnField("gas")
    """"""
    GAS_PRICE = ColumnField("gas_price")
    """"""
    INPUT = ColumnField("input")
    """"""
    BLOCK_TIMESTAMP = ColumnField("block_timestamp")
    """"""
    MAX_FEE_PER_GAS = ColumnField("max_fee_per_gas")
    """"""
    MAX_PRIORITY_FEE_PER_GAS = ColumnField("max_priority_fee_per_gas")
    """"""
    TRANSACTION_TYPE = ColumnField("transaction_type")
    """"""
    BLOCK_NUMBER = ColumnField("block_number")
    """"""

    TYPE_MAPPER = {
        "hash": "str",
        "nonce": "int",
        "block_hash": "str",
        "transaction_index": "int",
        "from_address": "str",
        "to_address": "str",
        "value": "int",
        "gas": "int",
        "gas_price": "int",
        "input": "str",
        "block_timestamp": "str",
        "max_fee_per_gas": "int",
        "max_priority_fee_per_gas": "int",
        "transaction_type": "str",
        "block_number": "int",
    }

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    @property
    def bigint_cols(self) -> List[ColumnField]:
        return [self.VALUE, self.GAS_PRICE, self.MAX_FEE_PER_GAS, self.MAX_PRIORITY_FEE_PER_GAS]


class TokenTable(LedgerTable):
    """
    Tokens ledger data table
    Column names
    """

    ADDRESS = ColumnField("address")
    """"""
    SYMBOL = ColumnField("symbol")
    """"""
    NAME = ColumnField("name")
    """"""
    DECIMALS = ColumnField("decimals")
    """"""
    BLOCK_HASH = ColumnField("block_hash")
    """"""
    BLOCK_NUMBER = ColumnField("block_number")
    """"""
    BLOCK_TIMESTAMP = ColumnField("block_timestamp")
    """"""

    TYPE_MAPPER = {
        "address": "str",
        "symbol": "str",
        "name": "str",
        "decimals": "int",
        "block_hash": "str",
        "block_number": "int",
        "block_timestamp": "str",
    }

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    @property
    def bigint_cols(self) -> List[ColumnField]:
        return []


class TokenBalanceTable(LedgerTable):
    """
    Token balance ledger data table
    Column names
    """

    BLOCK_TIMESTAMP = ColumnField("block_timestamp")
    """"""
    BLOCK_HASH = ColumnField("block_hash")
    """"""
    BLOCK_NUMBER = ColumnField("block_number")
    """"""
    TOKEN_ADDRESS = ColumnField("token_address")
    """"""
    TRANSACTION_HASH = ColumnField("transaction_hash")
    """"""
    LOG_INDEX = ColumnField("log_index")
    """"""
    ADDRESS = ColumnField("address")
    """"""
    COUNTERPARTY_ADDRESS = ColumnField("counterparty_address")
    """"""
    RAW_AMOUNT = ColumnField("raw_amount")
    """Unscaled raw amount"""
    AMOUNT = ColumnField("amount")
    """Raw Amount scaled by token decimals"""

    TYPE_MAPPER = {
        "block_timestamp": "str",
        "block_hash": "str",
        "block_number": "int",
        "token_address": "str",
        "transaction_hash": "str",
        "log_index": "int",
        "address": "str",
        "from_address": "str",
        "to_address": "str",
        "raw_amount": "int",
        "amount": "int",
    }

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    @property
    def bigint_cols(self) -> List[ColumnField]:
        return [self.RAW_AMOUNT]


class TokenTransferTable(LedgerTable):
    """
    Token transfers ledger data table
    Column names
    """

    TOKEN_ADDRESS = ColumnField("token_address")
    """"""
    FROM_ADDRESS = ColumnField("from_address")
    """"""
    TO_ADDRESS = ColumnField("to_address")
    """"""
    RAW_AMOUNT = ColumnField("raw_amount")
    """"""
    USD_AMOUNT = ColumnField("usd_amount")
    """"""
    TRANSACTION_HASH = ColumnField("transaction_hash")
    """"""
    LOG_INDEX = ColumnField("log_index")
    """"""
    BLOCK_HASH = ColumnField("block_hash")
    """"""
    BLOCK_NUMBER = ColumnField("block_number")
    """"""
    BLOCK_TIMESTAMP = ColumnField("block_timestamp")
    """"""

    TYPE_MAPPER = {
        "token_address": "str",
        "from_address": "str",
        "to_address": "str",
        "raw_amount": "int",
        "usd_amount": "float",
        "transaction_hash": "str",
        "log_index": "int",
        "block_hash": "str",
        "block_number": "int",
        "block_timestamp": "str",
    }

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    @property
    def bigint_cols(self) -> List[ColumnField]:
        return [self.RAW_AMOUNT]


class TraceTable(LedgerTable):
    """
    Trace ledger data table
    Column names
    """

    BLOCK_HASH = ColumnField("block_hash")
    """"""
    BLOCK_NUMBER = ColumnField("block_number")
    """"""
    BLOCK_TIMESTAMP = ColumnField("block_timestamp")
    """"""
    TRANSACTION_HASH = ColumnField("transaction_hash")
    """"""
    TRANSACTION_INDEX = ColumnField("transaction_index")
    """"""
    FROM_ADDRESS = ColumnField("from_address")
    """"""
    TO_ADDRESS = ColumnField("to_address")
    """"""
    VALUE = ColumnField("value")
    """"""
    INPUT = ColumnField("input")
    """"""
    OUTPUT = ColumnField("output")
    """"""
    TRACE_TYPE = ColumnField("trace_type")
    """"""
    CALL_TYPE = ColumnField("call_type")
    """"""
    REWARD_TYPE = ColumnField("reward_type")
    """"""
    GAS = ColumnField("gas")
    """"""
    TRACE_ADDRESS = ColumnField("trace_address")
    """"""
    ERROR = ColumnField("error")
    """"""
    STATUS = ColumnField("status")
    """"""
    TRACE_ID = ColumnField("trace_id")
    """"""

    TYPE_MAPPER = {
        "block_hash": "str",
        "block_number": "int",
        "block_timestamp": "str",
        "transaction_hash": "str",
        "transaction_index": "int",
        "from_address": "str",
        "to_address": "str",
        "value": "int",
        "input": "str",
        "output": "str",
        "trace_type": "str",
        "call_type": "str",
        "reward_type": "Optional[str]",
        "gas": "int",
        "trace_address": "str",
        "error": "Optional[str]",
        "status": "int",
        "trace_id": "str",
    }

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    @property
    def bigint_cols(self) -> List[ColumnField]:
        return [self.VALUE]


JoinAllTypes = Union[
    tuple[JoinType, LedgerTable, str],
    tuple[LedgerTable, str],
    tuple[JoinType, LedgerTable, ColumnField],
    tuple[LedgerTable, ColumnField],
]
