class JumpCalculator:
    def __init__(self, har_strength: int) -> None:
        self.__har_strength = har_strength
        self.__mod_strength = (har_strength - 10) // 2

    def calc_jump_length(self, running_start: bool) -> float:
        return self.__har_strength if running_start else self.__har_strength / 2

    def calc_jump_height(self, running_start: bool) -> float:
        return 3 + self.__mod_strength if running_start else (3 + self.__mod_strength) / 2


class NegativeNumberError(Exception):
    def __init__(self, number):
        self.number = number
        super().__init__(f"Отрицательное число {number} не допустимо")

def check_positive_number(number):
    if number < 0:
        raise NegativeNumberError(number)
    else:
        return number


class ConverterCoins:
    def __init__(self, m=0, s=0, g=0, p=0) -> None:
        self.__points = self.convert_to_points(m, s, g, p)
        self.__m = m  # Медные
        self.__s = s  # Серебряные
        self.__g = g  # Золотые
        self.__p = p  # Платиновые

    @staticmethod
    def convert_to_points(m=0, s=0, g=0, p=0) -> int:
        return m + s * 10 + g * 100 + p * 10000

    def convert_to_coins(self) -> None:
        self.__p = self.__points // 10000
        self.__g = (self.__points - self.__p) // 100
        self.__s = (self.__points - self.__g) // 10
        self.__m = self.__points - self.__s

    def change_coins(self, operation: bool, m=0, s=0, g=0, p=0) -> None:
        # operation: True - Addition // False - Subtraction
        new_points = self.convert_to_points(m, s, g, p)
        if operation:
            self.__points += new_points
        else:
            try:
                result = self.__points - new_points
            except NegativeNumberError as e:
                print(e) # временно


    @property
    def m(self) -> int:
        return self.__m

    @m.setter
    def m(self, value: int) -> None:
        self.__m = value

    @property
    def s(self) -> int:
        return self.__s

    @s.setter
    def s(self, value: int) -> None:
        self.__s = value

    @property
    def g(self) -> int:
        return self.__g

    @g.setter
    def g(self, value: int) -> None:
        self.__g = value

    @property
    def p(self) -> int:
        return self.__p

    @p.setter
    def p(self, value: int) -> None:
        self.__p = value
