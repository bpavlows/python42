from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return sequence


def main() -> None:
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target}"

    def heal(target: str, power: int) -> str:
        return f"Heals {target}"

    def raw_power(target: str, power: int) -> str:
        return str(power)

    def is_powerful(target: str, power: int) -> bool:
        return power >= 50

    print("Testing spell combiner...")
    combo_spell = spell_combiner(fireball, heal)
    res1, res2 = combo_spell('Dragon', 0)
    print(f"Combined spell result: {res1}, {res2}")

    print("\nTesting power amplifier...")
    mega_spell = power_amplifier(raw_power, 3)
    print(f"Original: 10, Amplified: {mega_spell('Any', 10)}")

    print("\nTesting conditional caster...")
    safe_cast = conditional_caster(is_powerful, fireball)
    print(f"Cast with 30 power: {safe_cast('Orc', 30)}")
    print(f"Cast with 60 power: {safe_cast('Orc', 60)} for 60 damage")

    print("\nTesting spell sequence...")
    gatling_magic = spell_sequence([fireball, heal, fireball])
    seq_res = gatling_magic('Troll', 15)
    print(f"Sequence result: {seq_res}")


if __name__ == "__main__":
    main()
