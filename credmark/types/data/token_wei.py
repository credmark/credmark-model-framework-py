
class TokenWei(int):
    def __new__(cls, value, decimals: int):  # pylint: disable=unused-argument
        return int.__new__(cls, value)

    def __init__(self, value, decimals: int):
        int.__init__(value)
        self.decimals = decimals

    def __add__(self, __x):
        return TokenWei(super().__add__(__x), self.decimals)

    def __sub__(self, __x):
        return TokenWei(super().__sub__(__x), self.decimals)

    def __mul__(self, __x):
        return TokenWei(super().__mul__(__x), self.decimals)

    def __floordiv__(self, __x: int):
        return TokenWei(super().__floordiv__(__x), self.decimals)

    def __truediv__(self, __x: int):
        return TokenWei(super().__truediv__(__x), self.decimals)

    def __mod__(self, __x: int):
        return TokenWei(super().__mod__(__x), self.decimals)

    def __divmod__(self, __x: int):
        return TokenWei(super().__divmod__(__x), self.decimals)

    @property
    def scaled(self):
        return float(self) / (10 ** self.decimals)
