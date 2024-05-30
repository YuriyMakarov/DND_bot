class CharacteristicMinimumError(Exception):
    def __init__(self):
        super().__init__(f"Значение характеристики должно быть 5 или выше")


def get_jump_length(har_strength: int, running_start: bool) -> float:
    if har_strength >= 5:
        return har_strength if running_start else har_strength / 2
    else:
        raise CharacteristicMinimumError


def get_jump_height(har_strength: int, running_start: bool) -> float:
    if har_strength >= 5:
        mod_strength = (har_strength - 10) // 2
        return 3 + mod_strength if running_start else (3 + mod_strength) / 2
    else:
        raise CharacteristicMinimumError
