import alchemy


def main() -> None:
    print("=== Alembic 1 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print(f"Testing create_air: {alchemy.create_air()}")
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    print("Testing the hidden create_earth:", end=" ")
    print(alchemy.create_earth())


if __name__ == "__main__":
    main()
    
    
""" import alchemy
→ __init__.py arayüzü ex2 deki örnek bunu öğretmeyi amaçlıyordu

from alchemy.elements import ...
→ elements.py dosyasına doğrudan erişim 
Paket içindeki dosyaları doğrudan çalıştırmadım; relative import’ların doğru çalışması için proje kökünden
ft_transmutation_0.py dosyasını çalıştırdım
"""