from datetime import datetime


class BlockNumber(int):
    def __new__(cls, number: int = None, context=None, timestamp=None, sample_timestamp=None):
        if number is None:
            if sample_timestamp is not None:
                get_blocknumber_result = context.run_model(
                    'rpc.get-blocknumber', {"timestamp": sample_timestamp})
                return BlockNumber(number=get_blocknumber_result['blockNumber'],
                                   context=context,
                                   timestamp=get_blocknumber_result['blockTimestamp'],
                                   sample_timestamp=sample_timestamp)
        else:
            return super().__new__(BlockNumber, number)

    def __init__(self, number: int = None, context=None,
                 timestamp=None, sample_timestamp=None) -> None:
        self.context = context
        self._timestamp = timestamp
        self.sample_timestamp = sample_timestamp
        super().__init__()

    def __add__(self, number):
        return BlockNumber(super().__add__(number), self.context)

    def __sub__(self, number):
        return BlockNumber(super().__sub__(number), self.context)

    def __timestamp__(self) -> int:
        if self._timestamp is None:
            if self.context is not None:
                self._timestamp = self.context.web3.eth.get_block(self.__int__()).timestamp
        return self._timestamp

    def to_datetime(self):
        return datetime.fromtimestamp(self.__timestamp__())

    @ property
    def timestamp(self) -> int:
        return self.__timestamp__()

    @ property
    def datestring(self) -> str:
        return str(self.to_datetime())

    # TODO: Add checking that we aren't looking into the future
    # TODO: Add BlockRange type
