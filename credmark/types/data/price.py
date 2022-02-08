from .base.block_data import BlockData


class Price(BlockData):
    def __init__(self, token, value_usd):
        self.value_usd = value_usd
        self.token = token
