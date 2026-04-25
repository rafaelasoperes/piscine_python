from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def cast(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return cast


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list:
        return [spell(target, power) for spell in spells]
    return sequence


if __name__ == "__main__":
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} damage"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    def shield(target: str, power: int) -> str:
        return f"Shield protects {target} with {power} armor"

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 10)
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    original = fireball("Goblin", 10)
    amplified = mega_fireball("Goblin", 10)
    print("Original: 10, Amplified: 30")
    print(f"  -> {original}")
    print(f"  -> {amplified}")

    print("\nTesting conditional caster...")

    def is_powerful(target: str, power: int) -> bool:
        return power >= 50

    safe_fireball = conditional_caster(is_powerful, fireball)
    print(safe_fireball("Dragon", 100))
    print(safe_fireball("Dragon", 10))

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal, shield])
    results = sequence("Hero", 25)
    for r in results:
        print(f"  {r}")
