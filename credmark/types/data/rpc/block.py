

class Block():
    def __init__(self, block_number=None, timestamp=None):
        if block_number is not None:
            self.block_number = block_number
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def timestamp(self):
        if self.__timestamp is not None:
            return self.__timestamp

    @timestamp.setter
    def timestamp(self, value):
        if self.block_number is None:
            pass
        self.__timestamp = value
