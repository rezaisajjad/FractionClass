class Fraction(object):
    Numerator = None
    DeNumerator = None

    def __init__(self, Numerator: int, DeNumerator: int = 1):
        super(Fraction, self).__init__()
        gcd = Fraction.__gcd__(Numerator, DeNumerator)
        self.Numerator = Numerator // gcd
        self.DeNumerator = DeNumerator // gcd

    def __str__(self) -> str:
        return f"{self.Numerator}/{self.DeNumerator}"

    def __int__(self) -> int:
        return self.Numerator//self.DeNumerator

    def __float__(self) -> float:
        return self.Numerator/self.DeNumerator

    def __floor__(self) -> int:
        return int(self)

    def __ceil__(self) -> int:
        return int(self) if self.Numerator % self.DeNumerator == 0 else int(self)+1

    def __gcd__(a: int, b: int) -> int:
        if a < 0:
            a *= -1
        if b < 0:
            a *= -1
        while a != 0 and b != 0:
            if a > b:
                a %= b
            else:
                b %= a
        return a if a != 0 else b

    def __equalize__(self, other):
        other: Fraction = other
        self.DeNumerator, self.Numerator = other.DeNumerator, other.Numerator
        return self

    def copy(self):
        return Fraction(1).__equalize__(self)

    def __convertToFraction__(self):
        if type(self) is int:
            return Fraction(self)
        return self

    def __add__(self, other):
        other: Fraction = Fraction.__convertToFraction__(other)

        Numerator = self.Numerator*other.DeNumerator + self.DeNumerator*other.Numerator
        DeNumerator = self.DeNumerator * other.DeNumerator
        return Fraction(Numerator, DeNumerator)

    def __sub__(self, other):
        return self+(-other)

    def __mul__(self, other):
        other: Fraction = Fraction.__convertToFraction__(other)

        Numerator = self.Numerator*other.Numerator
        DeNumerator = self.DeNumerator * other.DeNumerator
        return Fraction(Numerator, DeNumerator)

    def __rmul__(self, other):
        return self*other

    def __truediv__(self, other):
        other: Fraction = Fraction.__convertToFraction__(other)
        return self * ~other

    def __floordiv__(self, other):
        res: Fraction = self/other
        res.Numerator //= res.DeNumerator
        res.DeNumerator = 1
        return res

    def __pow__(self, other: int):
        tmp: Fraction = Fraction(1)
        for _ in range(other):
            tmp *= self
        return tmp

    def __iadd__(self, other):
        self.__equalize__(self + other)
        return self

    def __isub__(self, other):
        self.__equalize__(self-other)
        return self

    def __imul__(self, other):
        self.__equalize__(self*other)
        return self

    def __idiv__(self, other):
        self.__equalize__(self/other)
        return self

    def __ifloordiv__(self, other):
        self.__equalize__(self//other)
        return self

    def __ipow__(self, other):
        self.__equalize__(self**other)
        return self

    def __invert__(self):
        return Fraction(self.DeNumerator, self.Numerator)

    def __pos__(self):
        return self.copy()

    def __neg__(self):
        return -1*self.copy()

    def __magnitude__(self, other) -> tuple[int, int]:
        other: Fraction = other
        res = Fraction(self.Numerator*other.DeNumerator,
                       self.DeNumerator*other.Numerator)
        return res.Numerator, res.DeNumerator

    def __compare__(self, other, func) -> bool:
        other: Fraction = Fraction.__convertToFraction__(other)
        self, other = self.__magnitude__(other)
        return func(self, other)

    def __lt__(self, other):
        return self.__compare__(other, int.__lt__)

    def __gt__(self, other):
        return self.__compare__(other, int.__gt__)

    def __le__(self, other):
        return self.__compare__(other, int.__le__)

    def __ge__(self, other):
        return self.__compare__(other, int.__ge__)

    def __eq__(self, other):
        return self.__compare__(other, int.__eq__)

    def __ne__(self, other):
        return self.__compare__(other, int.__ne__)


a = Fraction(1, 21)
b = Fraction(2, 7)

print(a > 5)
