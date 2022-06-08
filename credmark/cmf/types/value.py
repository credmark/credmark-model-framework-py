from typing import Union, List, Any

from credmark.dto import DTO


class ObjectDto(DTO):

    value: object

    def __eq__(self, __x):
        return self.value.__eq__(__x)

    def __ne__(self, __x):
        return self.value.__ne__(__x)

    def __hash__(self) -> int:
        return self.value.__hash__()

    def __format__(self, __format_spec: str) -> str:
        return self.value.__format__(__format_spec)


class NumberDto(ObjectDto):
    value: Union[int, float]

    def __init__(self, value: Union[int, float]) -> None:
        super().__init__(value=value)

    def __add__(self, number):
        return type(self)(self.value.__add__(number))

    def __sub__(self, number):
        return type(self)(self.value.__sub__(number))

    def __mul__(self, number):
        return type(self)(self.value.__mul__(number))

    def __floordiv__(self, number):
        return type(self)(self.value.__floordiv__(number))

    def __truediv__(self, number):
        return type(self)(self.value.__truediv__(number))

    def __mod__(self, number):
        return type(self)(self.value.__mod__(number))

    def __divmod__(self, number):
        (__x, __y) = self.value.__divmod__(number)
        return (type(self)(__x), type(self)(__y))

    def __pow__(self, __x: int, __mod: None = None):
        return type(self)(self.value.__pow__(__x, __mod))

    def __ceil__(self):
        return type(self)(self.value.__ceil__())

    def __floor__(self):
        return type(self)(self.value.__floor__())

    def __round__(self):
        return type(self)(self.value.__round__())

    def __gt__(self, __x):
        return self.value.__gt__(__x)

    def __lt__(self, __x):
        return self.value.__lt__(__x)

    def __ge__(self, __x):
        return self.value.__ge__(__x)

    def __le__(self, __x):
        return self.value.__le__(__x)

    def __abs__(self):
        return type(self)(self.value.__abs__())

    def __neg__(self):
        return type(self)(self.value.__neg__())

    def __pos__(self):
        return type(self)(self.value.__pos__())

    def __int__(self):
        return type(self)(self.value.__int__())

    def __float__(self):
        return type(self)(self.value.__float__())


class TestNest(DTO):
    test_val: NumberDto
