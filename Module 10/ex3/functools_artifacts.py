import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    ops: dict[str, Callable[[Any, Any], Any]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": lambda a, b: max(a, b),
        "min": lambda a, b: min(a, b),
    }
    if operation not in ops:
        raise ValueError(f"Unknown operation: {operation}")
    return functools.reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire = functools.partial(base_enchantment, 50, "fire")
    water = functools.partial(base_enchantment, 50, "water")
    earth = functools.partial(base_enchantment, 50, "earth")
    return {"fire": fire, "water": water, "earth": earth}


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def dispatch(data: Any) -> str:
        return "Unknown spell type"

    @dispatch.register(int)
    def _(data: int) -> str:
        return f"Damage spell: {data} damage"

    @dispatch.register(str)
    def _(data: str) -> str:
        return f"Enchantment: {data}"

    @dispatch.register(list)
    def _(data: list) -> str:
        return f"Multi-cast: {len(data)} spells"

    return dispatch


def main() -> None:
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")
    print()

    print("Testing partial enchanter...")

    def base_enchant(power: int, element: str, target: str) -> str:
        return f"Enchanted {target} with {element} (Power {power})"
    enchants = partial_enchanter(base_enchant)
    print(enchants['fire']('Sword'))
    print()

    print("Testing memoized fibonacci...")
    for n in [0, 1, 10, 15]:
        print(f"Fib({n}): {memoized_fibonacci(n)}")
    print()

    print("Testing spell dispatcher...")
    dispatch = spell_dispatcher()
    print(dispatch(42))
    print(dispatch('fireball'))
    print(dispatch([1, 2, 3]))
    print(dispatch(3.14))


if __name__ == "__main__":
    main()
