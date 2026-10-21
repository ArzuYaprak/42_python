from abc import ABC, abstractmethod

from ex3.creature import Creature
from ex3.capabilities import TransformCapability

class InvalidStrategyError(Exception):
    pass#Exception sınıfından miras alarak bu duruma özel bir hata türü oluşturuyoruz.
        #Ek davranış gerekmediği için gövdesinde pass yeterli.

class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...

    @abstractmethod
    def act(self, creature: Creature) -> None:
        ...

class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)#isinstance(), bir nesnenin belirtilen sınıfa veya o sınıftan türeyen bir sınıfa ait olup olmadığını kontrol eder. Sonuç True veya False olur.

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                "Invalid entity for this normal strategy"
            )

        print(creature.attack())
        
class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not isinstance(creature, TransformCapability):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                "for this aggressive strategy"
            )

        print(creature.transform())
        print(creature.attack())
        print(creature.revert())