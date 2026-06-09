from abc import ABC, abstractmethod
from typing import cast
from ex0.creatures import Creature
from ex1.capabilities import HealCapability, TransformCapability


class InvalidStrategyError(Exception):
    pass


class BattleStrategy(ABC):
    name: str

    @abstractmethod
    def act(self, creature: Creature) -> list[str]:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    def _raise_if_invalid(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                    f"Invalid Creature '{creature.name}' "
                    f"for this {self.name} strategy"
                )


class NormalStrategy(BattleStrategy):
    name = "normal"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> list[str]:
        self._raise_if_invalid(creature)
        return [creature.attack()]


class AggressiveStrategy(BattleStrategy):
    name = "aggressive"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> list[str]:
        self._raise_if_invalid(creature)
        transform_creature = cast(TransformCapability, creature)
        return [
                transform_creature.transform(),
                creature.attack(),
                transform_creature.revert()
        ]


class DefensiveStrategy(BattleStrategy):
    name = "defensive"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> list[str]:
        self._raise_if_invalid(creature)
        healing_creature = cast(HealCapability, creature)
        return [creature.attack(), healing_creature.heal()]
