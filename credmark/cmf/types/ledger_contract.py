from enum import Enum
from typing import Any, Dict, List, Optional, Tuple, Union

import credmark.cmf.model
from credmark.cmf.model.errors import ModelInputError, ModelRunError

from .abi import ABI
from .ledger import ColumnField, JoinAllTypes, LedgerModelOutput, LedgerTable
from .ledger_query import LedgerQueryBase


class ContractFunctionsTable(LedgerTable):
    """
    Contract functions ledger data table
    Column names common to all functions
    Function-specific columns are added from ABI.
    """

    BLOCK_NUMBER = ColumnField('block_number')
    """"""
    BLOCK_TIMESTAMP = ColumnField('block_timestamp')
    """"""
    TRACE_ADDRESS = ColumnField('trace_address')
    """"""
    FROM_ADDRESS = ColumnField('from_address')
    """"""
    TO_ADDRESS = ColumnField('to_address')
    """"""
    TXN_HASH = ColumnField('transaction_hash')
    """"""
    SIGNATURE = ColumnField('signature')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def bigint_cols(self):
        return [v for k, v in self._column_dict.items() if k.startswith('FN_')]


class ContractEventsTable(LedgerTable):
    """
    Contract events ledger data table
    Column names common to all events
    Event-specific columns are added from ABI.
    """

    BLOCK_NUMBER = ColumnField('block_number')
    """"""
    BLOCK_TIMESTAMP = ColumnField('block_timestamp')
    """"""
    LOG_INDEX = ColumnField('log_index')
    """"""
    CONTRACT_ADDRESS = ColumnField('contract_address')
    """"""
    TXN_HASH = ColumnField('transaction_hash')
    """"""
    SIGNATURE = ColumnField('signature')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def bigint_cols(self):
        return [v for k, v in self._column_dict.items() if k.startswith('EVT_')]


class ContractEntityType(Enum):

    """"""
    FUNCTIONS = 'functions'
    """"""
    EVENTS = 'events'
    """"""


class ContractEntityQuery(LedgerQueryBase):
    """
    Used by :class:`~credmark.cmf.types.ledger.ContractLedger` to query a
    contract's function or event data.
    You do not need to create an instance yourself.

    Access an instance with ``contract.ledger.functions.{NameOfFunction}``
    or ``contract.ledger.events.{NameOfEvent}``. The name of the function or event
    can be auto-completed by pressing TAB after the ``.``. Alternatively, you could
    looked the name of the function/event up from ``contract.abi.functions`` or
    `contract.abi.events`.

    See the :meth:`~credmark.cmf.types.ledger_contract.ContractEntityQuery.select`
    method below for the query parameters.

    Parameters:
        address: Contract address

        entity_type: Type of entity: functions or events

        name: Name of function or event
    """

    def __init__(self, **kwargs):
        """"""
        self._address = kwargs['address']
        self._entity_type = kwargs['entity_type']
        self._name = kwargs['name']
        super().__init__()

    def select(self,  # pylint: disable=too-many-arguments
               columns: Optional[Union[List[str], List[ColumnField]]] = None,
               joins: Optional[list[JoinAllTypes]] = None,
               where: Optional[str] = None,
               group_by: Optional[Union[List[str], List[ColumnField]]] = None,
               order_by: Optional[Union[str, ColumnField]] = None,
               limit: Optional[int] = None,
               offset: Optional[int] = None,
               aggregates: Optional[List[Tuple[str, str]]] = None,
               having: Optional[str] = None,
               bigint_cols: Optional[List[str]] = None) -> LedgerModelOutput:
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

            with contract.ledger.functions.approve as q:
                ret = q.select(
                    aggregates=[(q.VALUE.max_(), 'max_value')],
                    group_by=[q.SPENDER],
                    order_by=q.field('max_value').dquote().desc(),
                    limit=5)
            # ret.data contains a list of row dicts, keyed by column name
        """
        if self._entity_type == ContractEntityType.FUNCTIONS:
            model_slug = 'contract.function_data'
        elif self._entity_type == ContractEntityType.EVENTS:
            model_slug = 'contract.event_data'
        else:
            raise ValueError(
                f'Invalid ContractLedger entity type {self._entity_type}')

        context = credmark.cmf.model.ModelContext.current_context()

        model_input = self._gen_model_input(
            model_slug=model_slug,
            originator=context.__dict__['slug'],
            columns=columns,
            joins=joins,
            where=where,
            group_by=group_by,
            order_by=order_by,
            limit=limit,
            offset=offset,
            aggregates=aggregates,
            having=having)

        if self._entity_type == ContractEntityType.FUNCTIONS:
            model_input['functionName'] = self._name
        elif self._entity_type == ContractEntityType.EVENTS:
            model_input['eventName'] = self._name

        model_input['contractAddress'] = self._address

        # pylint:disable=no-member, protected-access
        model_input['l2_columns'] = self.bigint_cols  # type: ignore

        ledger_out = context.run_model(slug=model_slug,
                                       input=model_input,
                                       return_type=LedgerModelOutput)

        # pylint:disable=no-member, protected-access
        ledger_out.set_bigint_cols(
            self.bigint_cols +  # type: ignore
            ([] if bigint_cols is None else bigint_cols))
        return ledger_out


class LedgerQueryContractFunctions(ContractFunctionsTable, ContractEntityQuery):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class LedgerQueryContractEvents(ContractEventsTable, ContractEntityQuery):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


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

    All event/function-specific fields are loaded as character
    to preserve its full precision for integer types.
    They will be converted back to integer with .to_dataframe().
    """

    def __init__(self, address: str, abi: ABI):
        super().__init__()
        self._address = address
        self._abi = abi

    @property
    def functions(self):
        return ContractEntityFactory(
            ContractEntityType.FUNCTIONS, self._address, self._abi)

    @property
    def events(self):
        return ContractEntityFactory(
            ContractEntityType.EVENTS, self._address, self._abi)


class ContractEntityFactory:
    def __init__(self, entity_type: ContractEntityType, address: str, abi: ABI):
        super().__init__()
        self.entity_type = entity_type
        self.address = address
        self.abi = abi

    def decoded_cols(self,
                     prefix: Tuple[str, str],
                     names: List[Dict[str, Any]]) -> List[Tuple[str, str]]:
        more_cols = []
        unnamed_sn = 0
        for n, _ in enumerate(names):
            if names[n]['name'] == '':
                more_cols.append((f"{prefix[0]}__{unnamed_sn}",
                                  f'{prefix[1]}__{unnamed_sn}'))
                unnamed_sn += 1
            else:
                more_cols.append((f"{prefix[0]}_{names[n]['name'].upper()}",
                                  f'{prefix[1]}_{names[n]["name"]}'))
        return more_cols

    def __dir__(self):
        if self.entity_type == ContractEntityType.FUNCTIONS:
            return self.abi.functions.names()
        elif self.entity_type == ContractEntityType.EVENTS:
            return self.abi.events.names()
        raise ModelRunError(
            f'All types of {self.entity_type=} should be covered')

    def __repr__(self):
        return self.__class__.__name__ + ' ' + str(dir(self))

    def _ipython_key_completions_(self):
        return dir(self)

    def __getattr__(self, _name: str):
        if self.entity_type == ContractEntityType.FUNCTIONS:
            if self.abi.functions is None:
                raise ModelInputError(f'ABI for {self.address} is not loaded')

            if _name in self.abi.functions:
                more_cols = self.decoded_cols(
                    ('FN', 'fn'), self.abi.functions[_name]['inputs'])

                return LedgerQueryContractFunctions(
                    address=self.address,
                    entity_type=self.entity_type,
                    name=_name,
                    table_key='fn',
                    more_cols=more_cols)

        elif self.entity_type == ContractEntityType.EVENTS:
            if self.abi.events is None:
                raise ModelInputError(f'ABI for {self.address} is not loaded')

            if _name in self.abi.events:
                more_cols = self.decoded_cols(
                    ('EVT', 'evt'), self.abi.events[_name]['inputs'])

                return LedgerQueryContractEvents(
                    address=self.address,
                    entity_type=self.entity_type,
                    name=_name,
                    table_key='evt',
                    more_cols=more_cols)

        raise AttributeError(_name)
