def calculate_ability_mod(ability_score: int) -> int:
    ability_mod = int((ability_score - 10) / 2)
    return ability_mod

