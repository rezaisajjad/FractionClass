class Fraction(object):
    Numerator = None
    DeNumerator = None

    def __init__(self, Numerator: int, DeNumerator: int = 1):
        super(Fraction, self).__init__()
        gcd = Fraction.__gcd__(Numerator, DeNumerator)
        Numerator //= gcd
        DeNumerator //= gcd
        self.Numerator = Numerator
        self.DeNumerator = DeNumerator

    def __str__(self) -> str:
        return f"{self.Numerator}/{self.DeNumerator}"

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
        self: Fraction = self
        other: Fraction = other

        self.DeNumerator = other.DeNumerator
        self.Numerator = other.Numerator
        return self

    def copy(self):
        return Fraction(1).__equalize__(self)

    def __add__(self, other):
        self: Fraction = self
        other: Fraction = other
        if type(other) is int:
            other = Fraction(other)
        Numerator = self.Numerator*other.DeNumerator + self.DeNumerator*other.Numerator
        DeNumerator = self.DeNumerator * other.DeNumerator
        return Fraction(Numerator, DeNumerator)

    def __sub__(self, other):
        other = other*-1
        return self+other

    def __mul__(self, other):
        self: Fraction = self
        other: Fraction = other
        if type(other) is int:
            other = Fraction(other)
        Numerator = self.Numerator*other.Numerator
        DeNumerator = self.DeNumerator * other.DeNumerator
        return Fraction(Numerator, DeNumerator)

    def __rmul__(self, other):
        return self*other

    def __truediv__(self, other):
        return self * (~other)

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
        self: Fraction = self
        other: Fraction = other
        res = Fraction(self.Numerator*other.DeNumerator,
                       self.DeNumerator*other.Numerator)
        return res.Numerator, res.DeNumerator

    def __compare__(self, other, func) -> bool:
        if type(other) is int:
            other = Fraction(other)
        magnitude: tuple(int, int) = self.__magnitude__(other)
        self: int = magnitude[0]
        other: int = magnitude[1]
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
