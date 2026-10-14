def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    
    allowed_ingredients: list[str] = (
        light_spell_allowed_ingredients()
    )
    lowered_ingredients: str = ingredients.lower()#komple listeyi bir stringe çeviriyoruz hepsi küçük harfli olacak şekilde sonra o stringin içerisinde ingredient i arıyoruz
    
    for ingredient in allowed_ingredients:
        if ingredient in lowered_ingredients:
            return "VALID"
        
    return "INVALID"