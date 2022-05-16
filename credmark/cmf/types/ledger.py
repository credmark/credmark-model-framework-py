from enum import Enum
from typing import List, Set, Union
import inspect
from credmark.dto import DTO, DTOField, PrivateAttr, IterableListGenericDTO
import credmark.cmf.model
import pandas as pd


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
    _iterator: str = PrivateAttr("data")

    def to_df(self):
        return pd.DataFrame(self.data)


class LedgerTable:
    """
    Base class for ledger data tables
    """

    class Columns:
        # Subclasses should have class properties for the column names.
        # Use a doc string """""" after each property so they will be
        # documented automatically.
        pass

    __column_set: Union[Set[str], None] = None

    @classmethod
    def columns(cls):
        """
        Return the set of columns for the table.

        For contract ledger tables, the set will not
        include any contract-specific columns.
        """
        if cls.__column_set is None:
            cls.__column_set = set()
            for i in inspect.getmembers(cls.Columns):
                if i[0][0].isalpha():
                    cls.__column_set.add(i[1])
        return cls.__column_set

    def __init__(self):
        pass


class TransactionTable(LedgerTable):
    """Transactions ledger data table"""
    class Columns:
        """Column names"""
        HASH = 'hash'
        """"""
        NONCE = 'nonce'
        """"""
        BLOCK_HASH = 'block_hash'
        """"""
        TRANSACTION_INDEX = 'transaction_index'
        """"""
        FROM_ADDRESS = 'from_address'
        """"""
        TO_ADDRESS = 'to_address'
        """"""
        VALUE = 'value'
        """"""
        GAS = 'gas'
        """"""
        GAS_PRICE = 'gas_price'
        """"""
        INPUT = 'input'
        """"""
        BLOCK_TIMESTAMP = 'block_timestamp'
        """"""
        MAX_FEE_PER_GAS = 'max_fee_per_gas'
        """"""
        MAX_PRIORITY_FEE_PER_GAS = 'max_priority_fee_per_gas'
        """"""
        TRANSACTION_TYPE = 'transaction_type'
        """"""
        BLOCK_NUMBER = 'block_number'
        """"""


class TraceTable(LedgerTable):
    """Trace ledger data table"""
    class Columns:
        """Column names"""
        BLOCK_NUMBER = 'block_number'
        """"""
        TRANSACTION_HASH = 'transaction_hash'
        """"""
        TRANSACTION_INDEX = 'transaction_index'
        """"""
        FROM_ADDRESS = 'from_address'
        """"""
        TO_ADDRESS = 'to_address'
        """"""
        VALUE = 'value'
        """"""
        INPUT = 'input'
        """"""
        OUTPUT = 'output'
        """"""
        TRACE_TYPE = 'trace_type'
        """"""
        CALL_TYPE = 'call_type'
        """"""
        REWARD_TYPE = 'reward_type'
        """"""
        GAS = 'gas'
        """"""
        GAS_USED = 'gas_used'
        """"""
        SUB_TRACES = 'sub_traces'
        """"""
        TRACE_ADDRESS = 'trace_address'
        """"""
        ERROR = 'error'
        """"""
        STATUS = 'status'
        """"""
        TRACE_ID = 'trace_id'
        """"""


class BlockTable(LedgerTable):
    """Blocks ledger data table"""
    class Columns:
        """Column names"""
        NUMBER = 'number'
        """"""
        HASH = 'hash'
        """"""
        PARENT_HASH = 'parent_hash'
        """"""
        NONCE = 'nonce'
        """"""
        SHA3_UNCLES = 'sha3_uncles'
        """"""
        LOGS_BLOOM = 'logs_bloom'
        """"""
        TRANSACTIONS_ROOT = 'transactions_root'
        """"""
        STATE_ROOT = 'state_root'
        """"""
        RECEIPTS_ROOT = 'receipts_root'
        """"""
        MINER = 'miner'
        """"""
        DIFFICULTY = 'difficulty'
        """"""
        TOTAL_DIFFICULTY = 'total_difficulty'
        """"""
        SIZE = 'size'
        """"""
        EXTRA_DATA = 'extra_data'
        """"""
        GAS_LIMIT = 'gas_limit'
        """"""
        GAS_USED = 'gas_used'
        """"""
        TIMESTAMP = 'timestamp'
        """"""
        TS = 'ts'
        """"""
        TRANSACTION_COUNT = 'transaction_count'
        """"""
        BASE_FEE_PER_GAS = 'base_fee_per_gas'
        """"""


class ContractTable(LedgerTable):
    """Contracts ledger data table"""
    class Columns:
        """Column names"""
        ADDRESS = 'address'
        """"""
        BYTECODE = 'bytecode'
        """"""
        FUNCTION_SIGHASHES = 'function_sighashes'
        """"""
        IS_ERC20 = 'is_erc20 '
        """"""
        IS_ERC721 = 'is_erc721 '
        """"""
        BLOCK_NUMBER = 'block_number'
        """"""


class LogTable(LedgerTable):
    """Logs ledger data table"""
    class Columns:
        """Column names"""
        LOG_INDEX = 'log_index'
        """"""
        TRANSACTION_HASH = 'transaction_hash'
        """"""
        TRANSACTION_INDEX = 'transaction_index'
        """"""
        BLOCK_HASH = 'block_hash'
        """"""
        BLOCK_NUMBER = 'block_number'
        """"""
        ADDRESS = 'address'
        """"""
        DATA = 'data'
        """"""
        TOPICS = 'topics'
        """"""


class ReceiptTable(LedgerTable):
    """Receipts ledger data table"""
    class Columns:
        """Column names"""
        TRANSACTION_HASH = 'transaction_hash'
        """"""
        TRANSACTION_INDEX = 'transaction_index'
        """"""
        BLOCK_HASH = 'block_hash'
        """"""
        BLOCK_NUMBER = 'block_number'
        """"""
        CUMULATIVE_GAS_USED = 'cumulative_gas_used'
        """"""
        GAS_USED = 'gas_used'
        """"""
        CONTRACT_ADDRESS = 'contract_address'
        """"""
        ROOT = 'root'
        """"""
        STATUS = 'status'
        """"""
        EFFECTIVE_GAS_PRICE = 'effective_gas_price'
        """"""


class TokenTable(LedgerTable):
    """Tokens ledger data table"""
    class Columns:
        """Column names"""
        ADDRESS = 'address'
        """"""
        SYMBOL = 'symbol'
        """"""
        NAME = 'name'
        """"""
        DECIMALS = 'decimals'
        """"""
        TOTAL_SUPPLY = 'total_supply'
        """"""
        BLOCK_NUMBER = 'block_number'
        """"""


class TokenTransferTable(LedgerTable):
    """Token transfers ledger data table"""
    class Columns:
        """Column names"""
        TOKEN_ADDRESS = 'token_address'
        """"""
        FROM_ADDRESS = 'from_address'
        """"""
        TO_ADDRESS = 'to_address'
        """"""
        VALUE = 'value'
        """"""
        TRANSACTION_HASH = 'transaction_hash'
        """"""
        LOG_INDEX = 'log_index'
        """"""
        BLOCK_NUMBER = 'block_number'
        """"""


class ContractFunctionsTable(LedgerTable):
    """Contract functions ledger data table"""

    # Column names are contract and function-specific but
    # the following and standard fields for all functions
    class Columns:
        """Column names"""
        CONTRACT_ADDRESS = 'contract_address'
        """"""
        TXN_BLOCK_NUMBER = 'txn_block_number'
        """"""
        TXN_HASH = 'txn_hash'
        """"""
        TXN_INDEX = 'txn_index'
        """"""
        SUCCESS = 'success'  # boolean indicating txn was successful or not
        """"""

    @classmethod
    def InputCol(cls, input_name: str):  # pylint: disable=invalid-name
        """Construct a column name from a function input name."""
        return f'inp_{input_name.lower()}'


class ContractEventsTable(LedgerTable):
    """Contract events ledger data table"""
    # Column names are contract and event-specific but
    # the following and standard fields for all events
    class Columns:
        """Column names"""
        CONTRACT_ADDRESS = 'contract_address'
        """"""
        EVT_BLOCK_NUMBER = 'evt_block_number'
        """"""
        EVT_HASH = 'evt_hash'
        """"""
        EVT_INDEX = 'evt_index'
        """"""

    @classmethod
    def InputCol(cls, input_name: str):  # pylint: disable=invalid-name
        """Construct a column name from an event input name."""
        return f'inp_{input_name.lower()}'


class ContractLedger:
    """
    Helper class used by :class:`~credmark.cmf.types.contract.Contract` for ledger queries
    on contract functions and events.

    You do not need to create an instance yourself.
    Access an instance from a :class:`credmark.cmf.types.contract.Contract`
    instance with ``contract.ledger``.

    See :class:`~credmark.cmf.types.ledger.ContractLedger.ContractEntity` below for info
    on running queries.

    Parameters:
        address: Contract address
    """
    Functions = ContractFunctionsTable
    """ContractFunctionsTable"""
    Events = ContractEventsTable
    """ContractEventsTable"""

    @classmethod
    def Aggregate(cls, expression: str, as_name: str):  # pylint: disable=invalid-name
        """
        Return a new :class:`credmark.cmf.types.ledger.LedgerAggregate` instance that can be used in
        an aggregates list.

        For example::

            aggregates=[
                ContractLedger.Aggregate(
                    f'MAX({ContractLedger.Functions.InputCol("value")})',
                    'max_value')
            ]

        Parameters:

            expression: an aggregate expression

            as_name: the column name for the returned aggregate data column
        """
        return LedgerAggregate(expression=expression, asName=as_name)

    class EntityType(Enum):
        """"""
        FUNCTIONS = 'functions'
        """"""
        EVENTS = 'events'
        """"""

    class ContractEntity:
        """
        Used by :class:`~credmark.cmf.types.ledger.ContractLedger` to query a
        contract's function or event data.
        You do not need to create an instance yourself.

        Access an instance with ``contract.ledger.functions.contractFunctionName()``
        or ``contract.ledger.events.contractEventName()`` where ``contractFunctionName``
        and ``contractEventName`` are the actual names of functions and events
        of the contract.

        See the :meth:`~credmark.cmf.types.ledger.ContractLedger.ContractEntity.__call__`
        method below for the query parameters.

        Parameters:
            address: Contract address

            entity_type: Type of entity: functions or events

            name: Name of function or event
        """

        def __init__(self, address: str, entity_type: 'ContractLedger.EntityType', name: str):
            """
            """
            super().__init__()
            self.address = address
            self.entity_type = entity_type
            self.name = name

        def __call__(self,  # pylint: disable=too-many-arguments
                     columns: Union[List[str], None] = None,
                     where: Union[str, None] = None,
                     group_by: Union[str, None] = None,
                     order_by: Union[str, None] = None,
                     limit: Union[str, None] = None,
                     offset: Union[str, None] = None,
                     aggregates: Union[List[LedgerAggregate], None] = None,
                     having: Union[str, None] = None) -> LedgerModelOutput:
            """
            Run a query on a contract's function or event data.

            Parameters:

                columns: The columns list should be built from ``ContractLedger.Functions.Columns``
                    and function input columns using
                    ``ContractLedger.Functions.InputCol('input-name')``
                    (where ``input-name`` is the name of an input for the particular contract
                    function.)
                    For events, use ``ContractLedger.Events.Columns`` and
                    ``ContractLedger.Events.InputCol()``.

                aggregates: The aggregates list should be built from ``ContractLedger.Aggregate()``
                    calls where the expression contains an SQL function (ex. MAX, SUM etc.) and
                    column names as described for the ``columns`` parameter.

                where: The where portion of an SQL query (without the word WHERE.)
                    The column names are as described for the ``columns`` parameter. Aggregate
                    column names must be in double-quotes.

                group_by: The "group by" portion of an SQL query (without the words "GROUP BY".)
                    The column names are as described for the ``columns`` parameter. Aggregate
                    column names must be in double-quotes.

                order_by: The "order by" portion of an SQL query (without the words "ORDER BY".)
                    The column names are as described for the ``columns`` parameter. Aggregate
                    column names must be in double-quotes.

                having: The "having" portion of an SQL query (without the word "HAVING".)
                    The column names are as described for the ``columns`` parameter. Aggregate
                    column names must be in double-quotes.

                limit: The "limit" portion of an SQL query (without the word "LIMIT".)
                    Typically this can be an integer as a string.

                offset: The "offset" portion of an SQL query (without the word "OFFSET".)
                    Typically this can be an integer as a string.

            Returns:
                An object with a ``data`` property which is a list
                of dicts, each dict holding a row with the keys being the column
                names. The column names can be referenced using
                ``ContractLedger.Functions.Columns``,
                ``ContractLedger.Functions.InputCol('...')``,
                and aggregate columns names.

            Example usage::

                contract = Contract(address='0x3a3a65aab0dd2a17e3f1947ba16138cd37d08c04')
                ret = contract.ledger.functions.approve(
                        columns=[ContractLedger.Functions.InputCol('spender')],
                        aggregates=[
                            ContractLedger.Aggregate(
                                f'MAX({ContractLedger.Functions.InputCol("value")})', 'max_value')
                        ],
                        group_by=ContractLedger.Functions.InputCol('spender'),
                        order_by='"max_value" desc',
                        limit='5')
                # ret.data contains a list of row dicts, keyed by column name
            """
            context = credmark.cmf.model.ModelContext.current_context()

            if columns is None:
                columns = []

            input = {'contractAddress': self.address,
                     'columns': columns,
                     'aggregates': aggregates,
                     'where': where,
                     'groupBy': group_by,
                     'having': having,
                     'orderBy': order_by,
                     'limit': limit,
                     'offset': offset}

            if self.entity_type == ContractLedger.EntityType.FUNCTIONS:
                model_slug = 'contract.function_data'
                input['functionName'] = self.name
            elif self.entity_type == ContractLedger.EntityType.EVENTS:
                model_slug = 'contract.event_data'
                input['eventName'] = self.name
            else:
                raise ValueError(f'Invalid ContractLedger entity type {self.entity_type}')

            return context.run_model(model_slug,
                                     input,
                                     return_type=LedgerModelOutput)

    class ContractEntityFactory:
        def __init__(self, entity_type: 'ContractLedger.EntityType', address: str):
            super().__init__()
            self.entity_type = entity_type
            self.address = address

        def __getattr__(self, __name: str) -> 'ContractLedger.ContractEntity':
            return ContractLedger.ContractEntity(self.address, self.entity_type, __name)

    def __init__(self, address: str):
        """
        """
        super().__init__()
        self.functions = ContractLedger.ContractEntityFactory(
            ContractLedger.EntityType.FUNCTIONS, address)
        self.events = ContractLedger.ContractEntityFactory(
            ContractLedger.EntityType.EVENTS, address)
