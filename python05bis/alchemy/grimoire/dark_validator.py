from .dark_spellbook import dark_spell_allowed_ingredients


def dark_validate_ingredients(ingredients: str) -> str:
    allowed_ingredients: list[str] = (
        dark_spell_allowed_ingredients()
    )
    lowered_ingredients: str = ingredients.lower()

    for ingredient in allowed_ingredients:
        if ingredient in lowered_ingredients:
            return "VALID"

    return "INVALID"