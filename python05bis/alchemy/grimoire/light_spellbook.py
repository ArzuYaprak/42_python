def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients #bunu dosyanın en üstüne yazsaydık validator da spellbook'u import ettiğinde circular import riski oluşabilirdi

    validation: str = validate_ingredients(ingredients)
    return f"Spell recorded: {spell_name} ({ingredients} - {validation})"