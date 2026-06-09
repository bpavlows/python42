from ex0 import AquaFactory, FlameFactory
from ex0.creatures import CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import AggressiveStrategy, DefensiveStrategy, NormalStrategy
from ex2.strategies import BattleStrategy, InvalidStrategyError


def run_tournament(
        opponents: list[tuple[CreatureFactory, BattleStrategy]]
        ) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    creatures = [
            (factory.create_base(), strategy)
            for factory, strategy in opponents
            ]
    try:
        for first_index in range(len(creatures)):
            for second_index in range(first_index + 1, len(creatures)):
                first_creature, first_strategy = creatures[first_index]
                second_creature, second_strategy = creatures[second_index]
                print()
                print("* Battle *")
                print(first_creature.describe())
                print(" vs.")
                print(second_creature.describe())
                print(" now fight!")
                for action in first_strategy.act(first_creature):
                    print(action)
                for action in second_strategy.act(second_creature):
                    print(action)
    except InvalidStrategyError as e:
        print(f"Battle error, aborting tournament: {e}")


def main() -> None:
    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    run_tournament([
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
        ])
    print()

    print("Tournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    run_tournament([
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
        ])
    print()
    print("Tournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    run_tournament([
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy())
        ])


if __name__ == "__main__":
    main()
