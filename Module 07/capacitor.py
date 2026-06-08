from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1 import HealCapability, TransformCapability


def main() -> None:
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

    print("Testing Creature with transform capability")

    print(" base:")
    factory2 = TransformCreatureFactory()
    base2 = factory2.create_base()
    print(base2.describe())
    print(base2.attack())
    if isinstance(base2, TransformCapability):
        print(base2.transform())
    print(base2.attack())
    if isinstance(base2, TransformCapability):
        print(base2.revert())

    print(" evolved:")
    evolved2 = factory2.create_evolved()
    print(evolved2.describe())
    print(evolved2.attack())
    if isinstance(evolved2, TransformCapability):
        print(evolved2.transform())
    print(evolved2.attack())
    if isinstance(evolved2, TransformCapability):
        print(evolved2.revert())
    print()


if __name__ == "__main__":
    main()
