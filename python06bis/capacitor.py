from ex3 import TransformCreatureFactory


def main() -> None:
    factory = TransformCreatureFactory()

    print("Testing Creature with transform capability")
    print("base:")

    base = factory.create_base()

    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())
    print("\nevolved:")

    evolved = factory.create_evolved()

    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


if __name__ == "__main__":
    main()
    
"""Dönüşebilen fabrikanın hem temel hem gelişmiş yaratığı için sırayla:
1. Açıklamayı göster.
2. Normal saldırıyı göster.
3. Dönüştür.
4. Dönüşmüş durumdaki saldırıyı göster.
5. Normal duruma döndür.

yani dönüşüm yeteneğini test edeceğiz
"""