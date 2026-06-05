from . import HealCapability, TransformCapability
from ex0 import CreatureFactory
from ex0.creatures import Creature


class Sproutling(Creature, HealCapability):
    def __init__(self, name: str, types: str, gun: str):
        super().__init__(name, types)
        self.gun = gun
    
    def attack(self):
        return f"{self.name} uses {self.gun}!"
    
    def heal(self, target: str | None = None) -> str:
        if target:
            return f"{self.name} heals {target}!"
        else:
            return f"{self.name} heals itself!"
    

class Bloomelle(Creature, HealCapability):
    def __init__(self, name: str, types: str, gun: str):
        super().__init__(name, types)
        self.gun = gun
    
    def attack(self):
        return f"{self.name} uses {self.gun}!"
    
    def heal(self, target: str | None = None) -> str:
        if target:
            return f"{self.name} heals {target}!"
        else:
            return f"{self.name} heals itself!"


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str, types: str, gun: str):
        super().__init__(name, types)
        self.gun = gun
    
    def attack(self):
        return super().attack()
    
    def transform(self) -> str:
        return f"{self.name} transforms into a more powerful form!"

    def revert(self) -> str:
        return f"{self.name} reverts back to its original form!"


class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str, types: str, gun: str):
        super().__init__(name, types)
        self.gun = gun

    def attack(self):
        return super().attack()

    def transform(self) -> str:
        return f"{self.name} transforms into a more powerful form!"

    def revert(self) -> str:
        return f"{self.name} reverts back to its original form!"


class HealingCreatureFactory(CreatureFactory):



class  TransformCreatureFactory(CreatureFactory):