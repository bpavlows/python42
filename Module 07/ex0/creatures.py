from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, types: str):
        self.name = name
        self.types = types

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.types} type Creature"


class Flameling (Creature):
    def __init__(self, name: str, types: str, gun: str):
        super().__init__(name, types)
        self.gun = gun

    def attack(self) -> str:
        return f"{self.name} uses {self.gun}!"


class Pyrodon (Creature):
    def __init__(self, name: str, types: str, gun: str):
        super().__init__(name, types)
        self.gun = gun

    def attack(self) -> str:
        return f"{self.name} uses {self.gun}!"


class Aquabub (Creature):
    def __init__(self, name: str, types: str, gun: str):
        super().__init__(name, types)
        self.gun = gun

    def attack(self) -> str:
        return f"{self.name} uses {self.gun}!"


class Torragon (Creature):
    def __init__(self, name: str, types: str, gun: str):
        super().__init__(name, types)
        self.gun = gun

    def attack(self) -> str:
        return f"{self.name} uses {self.gun}!"


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flameling("Flameling", "Fire", "Ember")

    def create_evolved(self) -> Creature:
        return Pyrodon("Pyrodon", "Fire/Flying", "Flamethrower")


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Aquabub("Aquabub", "Water", "Water Gun")

    def create_evolved(self) -> Creature:
        return Torragon("Torragon", "Water", "Hydro Pump")
