import inspect


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
        HASH = 'HASH'
        NONCE = "NONCE",
        BLOCK_HASH = "BLOCK_HASH"
        TRANSACTION_INDEX = "TRANSACTION_INDEX"
        FROM_ADDRESS = "FROM_ADDRESS"
        TO_ADDRESS = "TO_ADDRESS"
        VALUE = "VALUE"
        GAS = "GAS"
        GAS_PRICE = "GAS_PRICE"
        INPUT = "INPUT"
        BLOCK_TIMESTAMP = "BLOCK_TIMESTAMP"
        MAX_FEE_PER_GAS = "MAX_FEE_PER_GAS"
        MAX_PRIORITY_FEE_PER_GAS = "MAX_PRIORITY_FEE_PER_GAS"
        TRANSACTION_TYPE = "TRANSACTION_TYPE"


class TraceTable(LedgerTable):
    class Columns:
        BLOCK_NUMBER = 'BLOCK_NUMBER'
        TRANSACTION_HASH = 'TRANSACTION_HASH'
        TRANSACTION_INDEX = 'TRANSACTION_INDEX'
        FROM_ADDRESS = 'FROM_ADDRESS'
        TO_ADDRESS = 'TO_ADDRESS'
        VALUE = 'VALUE'
        INPUT = 'INPUT'
        OUTPUT = 'OUTPUT'
        TRACE_TYPE = 'TRACE_TYPE'
        CALL_TYPE = 'CALL_TYPE'
        REWARD_TYPE = 'REWARD_TYPE'
        GAS = 'GAS'
        GAS_USED = 'GAS_USED'
        SUB_TRACES = 'SUB_TRACES'
        TRACE_ADDRESS = 'TRACE_ADDRESS'
        ERROR = 'ERROR'
        STATUS = 'STATUS'
        TRACE_ID = 'TRACE_ID'


class BlockTable(LedgerTable):
    class Columns:
        NUMBER = 'NUMBER'
        HASH = 'HASH'
        PARENT_HASH = 'PARENT_HASH'
        NONCE = 'NONCE'
        SHA3_UNCLES = 'SHA3_UNCLES'
        LOGS_BLOOM = 'LOGS_BLOOM'
        TRANSACTIONS_ROOT = 'TRANSACTIONS_ROOT'
        STATE_ROOT = 'STATE_ROOT'
        RECEIPTS_ROOT = 'RECEIPTS_ROOT'
        MINER = 'MINER'
        DIFFICULTY = 'DIFFICULTY'
        TOTAL_DIFFICULTY = 'TOTAL_DIFFICULTY'
        SIZE = 'SIZE'
        EXTRA_DATA = 'EXTRA_DATA'
        GAS_LIMIT = 'GAS_LIMIT'
        GAS_USED = 'GAS_USED'
        TIMESTAMP = 'TIMESTAMP'
        TS = 'TS'
        TRANSACTION_COUNT = 'TRANSACTION_COUNT'
        BASE_FEE_PER_GAS = 'BASE_FEE_PER_GAS'


class ContractTable(LedgerTable):
    class Columns:
        ADDRESS = 'ADDRESS'
        BYTECODE = 'BYTECODE'
        FUNCTION_SIGHASHES = 'FUNCTION_SIGHASHES'
        IS_ERC20 = 'IS_ERC20 '
        IS_ERC721 = 'IS_ERC721 '
        BLOCK_NUMBER = 'BLOCK_NUMBER'


class LogTable(LedgerTable):
    class Columns:
        LOG_INDEX = 'LOG_INDEX'
        TRANSACTION_HASH = 'TRANSACTION_HASH'
        TRANSACTION_INDEX = 'TRANSACTION_INDEX'
        BLOCK_HASH = 'BLOCK_HASH'
        BLOCK_NUMBER = 'BLOCK_NUMBER'
        ADDRESS = 'ADDRESS'
        DATA = 'DATA'
        TOPICS = 'TOPICS'


class ReceiptTable(LedgerTable):
    class Columns:
        TRANSACTION_HASH = 'TRANSACTION_HASH'
        TRANSACTION_INDEX = 'TRANSACTION_INDEX'
        BLOCK_HASH = 'BLOCK_HASH'
        BLOCK_NUMBER = 'BLOCK_NUMBER'
        CUMULATIVE_GAS_USED = 'CUMULATIVE_GAS_USED'
        GAS_USED = 'GAS_USED'
        CONTRACT_ADDRESS = 'CONTRACT_ADDRESS'
        ROOT = 'ROOT'
        STATUS = 'STATUS'
        EFFECTIVE_GAS_PRICE = 'EFFECTIVE_GAS_PRICE'


class TokenTable(LedgerTable):
    class Columns:
        ADDRESS = 'ADDRESS'
        SYMBOL = 'SYMBOL'
        NAME = 'NAME'
        DECIMALS = 'DECIMALS'
        TOTAL_SUPPLY = 'TOTAL_SUPPLY'
        BLOCK_NUMBER = 'BLOCK_NUMBER'


class TokenTransferTable(LedgerTable):
    class Columns:
        TOKEN_ADDRESS = 'TOKEN_ADDRESS'
        FROM_ADDRESS = 'FROM_ADDRESS'
        TO_ADDRESS = 'TO_ADDRESS'
        VALUE = 'VALUE'
        TRANSACTION_HASH = 'TRANSACTION_HASH'
        LOG_INDEX = 'LOG_INDEX'
        BLOCK_NUMBER = 'BLOCK_NUMBER'
