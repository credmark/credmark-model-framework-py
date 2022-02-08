from typing import List


class LedgerObject:
    columns = []

    def __init__(self):
        pass


class TransactionDefinition(LedgerObject):

    columns = [
        "hash",
        "nonce",
        "block_hash",
        "transaction_index",
        "from_address",
        "to_address",
        "value",
        "gas",
        "gas_price",
        "input",
        "block_timestamp",
        "max_fee_per_gas",
        "max_priority_fee_per_gas",
        "transaction_type"
    ]

    def __init__(self):
        super().__init__()


class BlockDefinition(LedgerObject):
    columns = [
        "number", "hash", "parent_hash", "nonce", "sha3_uncles", "logs_bloom", "transactions_root",
        "state_root", "receipts_root", "miner", "difficulty", "size", "extra_data", "total_difficulty",
        "size", "extra_data", "gas_limit", "gas_used", "timestamp", "transaction_count", "base_fee_per_gas"
    ]

    def __init__(self):
        super().__init__()
