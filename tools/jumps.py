def get_jump_length(har_strength: int, running_start: bool) -> float:
    return har_strength if running_start else har_strength / 2


def get_jump_height(har_strength: int, running_start: bool) -> float:
    mod_strength = (har_strength - 10) // 2
    return 3 + mod_strength if running_start else (3 + mod_strength) / 2
