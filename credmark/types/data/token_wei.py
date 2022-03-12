

class TokenWei(int):
    def __new__(cls, value, decimals: int):
        return int.__new__(cls, value)

    def __init__(self, value, decimals: int):
        int.__init__(value)
        self.decimals = decimals

    @property
    def scaled(self):
        return float(self) / (10 ** self.decimals)
