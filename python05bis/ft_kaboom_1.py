
def main() -> None:
    from alchemy.grimoire.dark_spellbook import dark_spell_record
    print(dark_spell_record("Darkness", "bats and arsenic"))


if __name__ == "__main__":
    print("=== Kaboom 1 ===")
    print(
        "Access to alchemy/grimoire/dark_spellbook.py directly"
    )
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    main()
    
"""dark_spellbook.py yükleniyor
    ↓
dark_validator.py import ediliyor
    ↓
dark_spellbook.py tekrar import ediliyor
    ↓
dark_spellbook.py henüz tamamlanmadı
    ↓
ImportError


Light:
import fonksiyon içinde → döngü kırılıyor → çalışıyor

Dark:
import dosya seviyesinde → circular import → ImportError


Dark grimoire’da iki modül birbirini dosya seviyesinde import ediyor.
Python bir modülü tamamen çalıştırmadan diğerini yüklemeye çalıştığı
için circular import oluşuyor. İkinci import sırasında ilk
modül henüz dark_spell_allowed_ingredients fonksiyonunu tanımlama
aşamasını tamamlamadığı için Python fonksiyonu bulamıyor ve ImportError veriyor.
    """