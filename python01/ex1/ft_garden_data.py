class Plant:
    # not: Sınıf, her bitkinin ortak verilerini ve davranışını topluyor.
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(plant) -> None:
        # not: plant burada self ile aynı rolde; self adı daha anlaşılır olur.
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")

    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
    ]

    for plant in plants:
        plant.show()#noktadan öncekini showa parametre olark gönderiyor ondan içersine yazmıyoruz
    
