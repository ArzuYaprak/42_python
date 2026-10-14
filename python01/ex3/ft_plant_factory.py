class Plant:
    # not: Aynı sınıftan farklı özelliklere sahip birçok nesne üretiyoruz.
    def __init__(self, name: str, height: float, age_days: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days
        
    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age_days} days old")
        
    def grow(self, growth: float) -> None:
        self.height += growth
        
    def age(self, day: int) -> None:
        self.age_days += day
        
if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plants = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120)
    ]
    
    for plant in plants:
        # not: Listedeki her nesne aynı show metodunu çağırabiliyor.
        print("Created: ", end="") 
        plant.show()
        
