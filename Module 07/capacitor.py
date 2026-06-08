from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capabilities import HealCapability, TransformCapability


def test_healing_factory(factory: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")

    print(" base:")
    factory = HealingCreatureFactory()
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    if isinstance(base, HealCapability):
        print(base.heal())

    print(" evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    if isinstance(evolved, HealCapability):
        print(evolved.heal())
    print()


def test_transform_factory(factory: TransformCreatureFactory) -> None:
    print("Testing Creature with transform capability")

    print(" base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    if isinstance(base, TransformCapability):
        print(base.transform())
    print(base.attack())
    if isinstance(base, TransformCapability):
        print(base.revert())

    print(" evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    if isinstance(evolved, TransformCapability):
        print(evolved.transform())
    print(evolved.attack())
    if isinstance(evolved, TransformCapability):
        print(evolved.revert())
    print()


def main() -> None:
    test_healing_factory(HealingCreatureFactory())
    test_transform_factory(TransformCreatureFactory())


if __name__ == "__main__":
    main()
