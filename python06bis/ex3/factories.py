from abc import ABC, abstractmethod

from .creature import Creature
from .entities import Flameling, Pyrodon, Shiftling, Morphagon

class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        ...

    @abstractmethod
    def create_evolved(self) -> Creature:
        ...
        
class FlameFactory(CreatureFactory):
    def create_base(self) -> Flameling:
        return Flameling()#yeni bir flaming nesnesi oluşturacak ve onu döndüreck şöyle olsaydı sınıfın kendisini döndürürdü return Flameling

    def create_evolved(self) -> Pyrodon:
        return Pyrodon()
    
class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()