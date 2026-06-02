def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients

    allowed = light_spell_allowed_ingredients()
    is_valid = any(item in ingredients.lower() for item in allowed)

    if is_valid:
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
