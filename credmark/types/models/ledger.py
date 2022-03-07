from typing import List
import inspect
from credmark.types.dto import DTO, DTOField, IterableListDto


class LedgerModelOutput(IterableListDto):
    data: List[dict] = DTOField([], description='A list of dicts which are the rows of data')
    iterator = "data"


class LedgerTable:

    class Columns:
        pass

    __column_set = None

    @classmethod
    def columns(cls):
        if cls.__column_set is None:
            cls.__column_set = set()
            for i in inspect.getmembers(cls.Columns):
                if i[0][0].isalpha():
                    cls.__column_set.add(i[1])
        return cls.__column_set

    def __init__(self):
        pass


class TransactionTable(LedgerTable):
    class Columns:
        HASH = 'hash'
        NONCE = 'nonce'
        BLOCK_HASH = 'block_hash'
        TRANSACTION_INDEX = 'transaction_index'
        FROM_ADDRESS = 'from_address'
        TO_ADDRESS = 'to_address'
        VALUE = 'value'
        GAS = 'gas'
        GAS_PRICE = 'gas_price'
        INPUT = 'input'
        BLOCK_TIMESTAMP = 'block_timestamp'
        MAX_FEE_PER_GAS = 'max_fee_per_gas'
        MAX_PRIORITY_FEE_PER_GAS = 'max_priority_fee_per_gas'
        TRANSACTION_TYPE = 'transaction_type'


class TraceTable(LedgerTable):
    class Columns:
        BLOCK_NUMBER = 'block_number'
        TRANSACTION_HASH = 'transaction_hash'
        TRANSACTION_INDEX = 'transaction_index'
        FROM_ADDRESS = 'from_address'
        TO_ADDRESS = 'to_address'
        VALUE = 'value'
        INPUT = 'input'
        OUTPUT = 'output'
        TRACE_TYPE = 'trace_type'
        CALL_TYPE = 'call_type'
        REWARD_TYPE = 'reward_type'
        GAS = 'gas'
        GAS_USED = 'gas_used'
        SUB_TRACES = 'sub_traces'
        TRACE_ADDRESS = 'trace_address'
        ERROR = 'error'
        STATUS = 'status'
        TRACE_ID = 'trace_id'


class BlockTable(LedgerTable):
    class Columns:
        NUMBER = 'number'
        HASH = 'hash'
        PARENT_HASH = 'parent_hash'
        NONCE = 'nonce'
        SHA3_UNCLES = 'sha3_uncles'
        LOGS_BLOOM = 'logs_bloom'
        TRANSACTIONS_ROOT = 'transactions_root'
        STATE_ROOT = 'state_root'
        RECEIPTS_ROOT = 'receipts_root'
        MINER = 'miner'
        DIFFICULTY = 'difficulty'
        TOTAL_DIFFICULTY = 'total_difficulty'
        SIZE = 'size'
        EXTRA_DATA = 'extra_data'
        GAS_LIMIT = 'gas_limit'
        GAS_USED = 'gas_used'
        TIMESTAMP = 'timestamp'
        TS = 'ts'
        TRANSACTION_COUNT = 'transaction_count'
        BASE_FEE_PER_GAS = 'base_fee_per_gas'


class ContractTable(LedgerTable):
    class Columns:
        ADDRESS = 'address'
        BYTECODE = 'bytecode'
        FUNCTION_SIGHASHES = 'function_sighashes'
        IS_ERC20 = 'is_erc20 '
        IS_ERC721 = 'is_erc721 '
        BLOCK_NUMBER = 'block_number'


class LogTable(LedgerTable):
    class Columns:
        LOG_INDEX = 'log_index'
        TRANSACTION_HASH = 'transaction_hash'
        TRANSACTION_INDEX = 'transaction_index'
        BLOCK_HASH = 'block_hash'
        BLOCK_NUMBER = 'block_number'
        ADDRESS = 'address'
        DATA = 'data'
        TOPICS = 'topics'


class ReceiptTable(LedgerTable):
    class Columns:
        TRANSACTION_HASH = 'transaction_hash'
        TRANSACTION_INDEX = 'transaction_index'
        BLOCK_HASH = 'block_hash'
        BLOCK_NUMBER = 'block_number'
        CUMULATIVE_GAS_USED = 'cumulative_gas_used'
        GAS_USED = 'gas_used'
        CONTRACT_ADDRESS = 'contract_address'
        ROOT = 'root'
        STATUS = 'status'
        EFFECTIVE_GAS_PRICE = 'effective_gas_price'


class TokenTable(LedgerTable):
    class Columns:
        ADDRESS = 'address'
        SYMBOL = 'symbol'
        NAME = 'name'
        DECIMALS = 'decimals'
        TOTAL_SUPPLY = 'total_supply'
        BLOCK_NUMBER = 'block_number'


class TokenTransferTable(LedgerTable):
    class Columns:
        TOKEN_ADDRESS = 'token_address'
        FROM_ADDRESS = 'from_address'
        TO_ADDRESS = 'to_address'
        VALUE = 'value'
        TRANSACTION_HASH = 'transaction_hash'
        LOG_INDEX = 'log_index'
        BLOCK_NUMBER = 'block_number'
