from .factories import (
    CreatureFactory,
    FlameFactory,
    TransformCreatureFactory
)#subject sadece factory kısmını dışarı açmamızı istiyor böylelikle test dosyalarında şöyle kullanabileceğiz: from ex3 import FlameFactory misal

__all__ = [
    "CreatureFactory",
    "FlameFactory",
    "TransformCreatureFactory"
]
#all import* dediğimizde all da ne varsa onlar gelir 
# misal all da 2 tane olsaydı 2 tane gelirdi ama all 3. 
# nün gelmesini engellemez onu da direkt from ex3 import adı ile import edebilirz