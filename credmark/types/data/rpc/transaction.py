
from .block import Block
from typing import Union

class Transaction():
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
    def __init__(self, **kwargs):
        pass



