from . import HealCapability, TransformCapability
from ex0 import CreatureFactory
from ex0.creatures import Creature


class Sproutling(Creature, HealCapability):
    def __init__(self, name: str, types: str, gun: str):
        super().__init__(name, types)
        self.gun = gun

    def attack(self) -> str:
        return f"{self.name} uses {self.gun}!"

    def heal(self) -> str:
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self, name: str, types: str, gun: str):
        super().__init__(name, types)
        self.gun = gun

    def attack(self) -> str:
        return f"{self.name} uses {self.gun}!"

    def heal(self) -> str:
        return f"{self.name} heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str, types: str):
        super().__init__(name, types)
        self.transformed = False

    def attack(self) -> str:
        if self.transformed:
            return "Shiftling performs a boosted strike!"
        return "Shiftling attacks normally."

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str, types: str):
        super().__init__(name, types)
        self.transformed = False

    def attack(self) -> str:
        if self.transformed:
            return f"{self.name} unleashes a devastating morph strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} stabilizes its form."


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Sproutling("Sproutling", "Grass", "Vine Whip")

    def create_evolved(self) -> Creature:
        return Bloomelle("Bloomelle", "Grass/Fairy", "Petal Dance")


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling("Shiftling", "Normal")

    def create_evolved(self) -> Creature:
        return Morphagon("Morphagon", "Normal/Dragon")
