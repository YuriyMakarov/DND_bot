class JumpCalculator:
    def __init__(self, har_strength: int) -> None:
        self.__har_strength = har_strength
        self.__mod_strength = (har_strength - 10) // 2

    def calc_jump_length(self, running_start: bool) -> float:
        return self.__har_strength if running_start else self.__har_strength / 2

    def calc_jump_height(self, running_start: bool) -> float:
        return 3 + self.__mod_strength if running_start else (3 + self.__mod_strength) / 2


class ConverterCoins:
    def __init__(self, m=0, s=0, g=0, p=0) -> None:
        self.__m = m  # Медные
        self.__s = s  # Серебряные
        self.__g = g  # Золотые
        self.__p = p  # Платиновые

    @staticmethod
    def convert_coins(small_coin, big_coin, rate):
        if small_coin > rate:
            big_coin += small_coin // rate
            small_coin = small_coin % rate
        return small_coin, big_coin

    def sorting_coins(self):
        self.__m, self.__s = self.convert_coins(self.__m, self.__s, 10)
        self.__s, self.__g = self.convert_coins(self.__s, self.__g, 10)
        self.__g, self.__p = self.convert_coins(self.__g, self.__p, 100)

    @property
    def m(self):
        return self.__m

    @m.setter
    def m(self, value: int):
        self.__m = value

    @property
    def s(self):
        return self.__s

    @s.setter
    def s(self, value: int):
        self.__s = value

    @property
    def g(self):
        return self.__g

    @g.setter
    def g(self, value: int):
        self.__g = value

    @property
    def p(self):
        return self.__p

    @p.setter
    def p(self, value: int):
        self.__p = value
