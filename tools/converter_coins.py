class NegativeNumberError(Exception):
    def __init__(self):
        super().__init__(f"Отрицательное число не допустимо")


def get_points(m_coin=0, s_coin=0, g_coin=0, p_coin=0) -> int:
    return m_coin + s_coin * 10 + g_coin * 100 + p_coin * 10000


def get_coins(points: int) -> tuple[int, int, int, int]:
    p = points // 10000
    g = (points - p * 10000) // 100
    s = (points - p * 10000 - g * 100) // 10
    m = points - p * 10000 - g * 100 - s * 10
    return m, s, g, p


def add_coins(points: int, m_coin=0, s_coin=0, g_coin=0, p_coin=0) -> int:
    return points + get_points(m_coin, s_coin, g_coin, p_coin)


def sub_coins(points: int, m_coin=0, s_coin=0, g_coin=0, p_coin=0) -> int:
    result = points - get_points(m_coin, s_coin, g_coin, p_coin)
    if result >= 0:
        return result
    else:
        raise NegativeNumberError
