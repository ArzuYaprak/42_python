import alchemy.grimoire


def main() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    print(
        "Testing record light spell: "
        f"{alchemy.grimoire.light_spell_record(
            'Fantasy',
            'Earth, wind and fire'
        )}"
    )


if __name__ == "__main__":
    main()
    
""""ft_kaboom_0.py
    ↓
alchemy.grimoire
    ↓
__init__.py → light_spell_record
    ↓
light_spellbook.py
    ↓
light_validator.py
    ↓
light_spellbook.py → izin listesi
Burada circular import’un çalışmasının nedeni, iki dosyanın birbirini import etmesine
rağmen import’ların fonksiyonların içinde yapılmasıdır. Bir sonraki adımda dark
grimoire’da bu import’ları bilerek dosya seviyesine taşıyıp patlayan örneği oluşturacağız.
"""