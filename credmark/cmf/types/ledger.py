import contextlib
import inspect
from enum import Enum
from typing import Dict, List, Optional, Tuple, Union

import credmark.cmf.model
import pandas as pd
from credmark.cmf.model.errors import ModelInputError
from credmark.dto import DTO, DTOField, IterableListGenericDTO, PrivateAttr

from .abi import ABI
from .block_number import BlockNumber

from credmark.cmf.model.ledger.errors import InvalidColumnException


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

    def to_dataframe(self):
        return pd.DataFrame(self.data)


class LedgerTable:
    """
    Base class for ledger data tables
    """

    # Use a doc string """""" after each property so they will be
    # documented automatically.

    __column_dict: Dict[str, str] = dict()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        print('__init__ledger_table_')
        self._more_cols = kwargs['more_cols']

        self.__column_dict = dict()
        for i in inspect.getmembers(self.__class__):
            if isinstance(getattr(self.__class__, i[0]), str) and i[0][0].isalpha():
                self.__column_dict[i[0]] = i[1]

        for i in self._more_cols:
            self.__column_dict[i[0]] = i[1]

    def __dir__(self):
        return list(self.__column_dict.keys()) + list(super().__dir__())

    def __repr__(self):
        return str(dir(self))

    def getitem(self, name):
        return self.__column_dict[name]

    @property
    def columns(self) -> List[str]:
        """
        Return the set of column names for the table.
        They will be used in the database.

        For contract ledger tables, the set will include
        all contract-specific columns.
        """
        return list(self.__column_dict.values())

    @property
    def colnames(self) -> List[str]:
        """
        Return the set of column names in the table.
        They can be used in the query.
        """

        return list(self.__column_dict.keys())

    def _validate_columns(self, model_slug: str,
                          columns: List[str]):

        column_set = set(self.columns)
        for column in columns:
            if column.lower() not in column_set:
                raise InvalidColumnException(
                    model_slug,
                    column, list(column_set), "invalid column name")


class TransactionTable(LedgerTable):
    """
    Transactions ledger data table
    Column names
    """

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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class TraceTable(LedgerTable):
    """
    Trace ledger data table
    Column names
    """

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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class BlockTable(LedgerTable):
    """
    Blocks ledger data table
    Column names
    """

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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ContractTable(LedgerTable):
    """
    Contracts ledger data table
    Column names
    """

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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class LogTable(LedgerTable):
    """
    Logs ledger data table
    Column names
    """

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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ReceiptTable(LedgerTable):
    """
    Receipts ledger data table
    Column names
    """

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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class TokenTable(LedgerTable):
    """
    Tokens ledger data table
    Column names
    """

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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class TokenTransferTable(LedgerTable):
    """
    Token transfers ledger data table
    Column names
    """

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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ContractFunctionsTable(LedgerTable):
    """
    Contract functions ledger data table
    Column names common to all functions
    Function-specific columns are added from ABI.
    """

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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ContractEventsTable(LedgerTable):
    """
    Contract events ledger data table
    Column names common to all events
    Event-specific columns are added from ABI.
    """

    CONTRACT_ADDRESS = 'contract_address'
    """"""
    EVT_BLOCK_NUMBER = 'evt_block_number'
    """"""
    EVT_HASH = 'evt_tx_hash'
    """"""
    EVT_INDEX = 'evt_index'
    """"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class LedgerQueryContractFunctions(ContractFunctionsTable, LedgerQuery):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class LedgerQueryContractEvents(ContractEventsTable, LedgerQuery):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ContractEntityFactory:
    def __init__(self, entity_type: 'ContractLedger.EntityType', address: str, abi: ABI):
        super().__init__()
        self.entity_type = entity_type
        self.address = address
        self.abi = abi

    def __dir__(self):
        if self.entity_type == ContractLedger.EntityType.FUNCTIONS:
            return self.abi.functions.names()
        elif self.entity_type == ContractLedger.EntityType.EVENTS:
            return self.abi.events.names()

    def __repr__(self):
        return self.__class__.__name__ + ' ' + str(dir(self))

    def _ipython_key_completions_(self):
        return dir(self)

    def __getattr__(self, _name: str) -> Optional['ContractLedger.ContractEntity']:
        if self.entity_type == ContractLedger.EntityType.FUNCTIONS:
            if self.abi.functions is None:
                raise ModelInputError(f'ABI for {self.address} is not loaded')

            if _name in self.abi.functions:
                more_cols = [(c['name'].upper(), f'inp_{c["name"]}')
                             for c in self.abi.functions[_name]['inputs']]
                return ContractLedger.ContractEntity(
                    self.address,
                    self.entity_type, _name,
                    ContractFunctionsTable(more_cols=more_cols))

        elif self.entity_type == ContractLedger.EntityType.EVENTS:
            if self.abi.events is None:
                raise ModelInputError(f'ABI for {self.address} is not loaded')

            if _name in self.abi.events:
                more_cols = [(c['name'].upper(), f'inp_{c["name"]}')
                             for c in self.abi.events[_name]['inputs']]
                return ContractLedger.ContractEntity(
                    self.address,
                    self.entity_type, _name,
                    ContractEventsTable(more_cols=more_cols))

        # raise ValueError(f'Invalid ContractLedger entity type {self.entity_type}')


class ContractLedger:
    # pylint: disable=locally-disabled,invalid-name

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

    class ContractEntity():
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

        def __enter__(self):
            return self

        def __exit__(self, *exc):
            return None

        @property
        def columns(self):
            """
            All columns in the table
            """
            return self._ledger_table.columns

        @property
        def colnames(self):
            """
            Column names to be used in the query
            """
            return self._ledger_table.colnames

        def dir__(self):
            return self._ledger_table.colnames + super().__dir__()

        def getattr__(self, name):
            if name in self._ledger_table.colnames:
                return self._ledger_table.getitem(name)

        def __init__(self, address: str,
                     entity_type: 'ContractLedger.EntityType',
                     name: str,
                     ledger_table):
            """"""
            super().__init__()
            self._address = address
            self._entity_type = entity_type
            self._name = name
            self._ledger_table = ledger_table

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

            model_input = {'contractAddress': self._address,
                           'columns': columns,
                           'aggregates': aggregates,
                           'where': where,
                           'groupBy': group_by,
                           'having': having,
                           'orderBy': order_by,
                           'limit': limit,
                           'offset': offset}

            if self._entity_type == ContractLedger.EntityType.FUNCTIONS:
                model_slug = 'contract.function_data'
                model_input['functionName'] = self._name
            elif self._entity_type == ContractLedger.EntityType.EVENTS:
                model_slug = 'contract.event_data'
                model_input['eventName'] = self._name
            else:
                raise ValueError(f'Invalid ContractLedger entity type {self._entity_type}')

            return context.run_model(model_slug,
                                     model_input,
                                     return_type=LedgerModelOutput)

    def __init__(self, address: str, abi: ABI):
        super().__init__()
        self._address = address
        self._abi = abi

    @property
    def functions(self):
        return ContractEntityFactory(
            ContractLedger.EntityType.FUNCTIONS, self._address, self._abi)

    @property
    def events(self):
        return ContractEntityFactory(
            ContractLedger.EntityType.EVENTS, self._address, self._abi)


class LedgerBlockTimeSeriesInput(DTO):
    """
    Input for the ledger.block-time-series model.
    """
    endTimestamp: int = DTOField(
        description='End timestamp of block series, inclusive unless exclusive is True')
    interval: int = DTOField(description='Series interval in seconds')
    count: int = DTOField(description='Number of intervals in the series.')
    exclusive: Union[bool, None] = DTOField(
        default=False, description='If true, blocks are exclusive of end timestamp')


class LedgerBlockNumberTimeSeries(DTO):
    """
    Output for the ledger.block-time-series model.
    """
    endTimestamp: int = DTOField(
        description='End timestamp of block series, inclusive unless exclusive is True')
    interval: int = DTOField(description='Series interval in seconds')
    exclusive: Union[bool, None] = DTOField(
        default=False, description='If true, blocks are exclusive of end timestamp')
    blockNumbers: List[BlockNumber] = DTOField(
        default=[],
        description='List of block numbers'
    )
