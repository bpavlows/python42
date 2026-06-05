from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test(creature) -> None:
    print("Testing factory")
    base = creature.create_base()
    evolved = creature.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    fighter_1 = factory1.create_base()
    fighter_2 = factory2.create_base()
    print("Testing battle")
    print(fighter_1.describe())
    print(" vs.")
    print(fighter_2.describe())
    print(" fight!")
    print(fighter_1.attack())
    print(fighter_2.attack())


def main() -> None:
    flame = FlameFactory()
    aqua = AquaFactory()
    test(flame)
    print()
    test(aqua)
    print()
    battle(flame, aqua)


if __name__ == "__main__":
    main()
