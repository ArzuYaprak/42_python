class Plant:
    # not: Bu egzersizde height ve age_days değerleri zamanla değişiyor.
    def __init__(self, name: str, height: float, age_days: int) -> None:
      self.name = name
      self.height = height
      self.age_days = age_days

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age_days} days old")
        
    def grow(self, growth: float) -> None:
        # not: += mevcut yüksekliğe büyüme miktarını ekler.
        self.height += growth
        
    def age(self, day: int) -> None:
        # not: Yaş da aynı nesnenin içinde güncelleniyor.
        self.age_days += day
    
if __name__ == "__main__":
    plant = Plant("Rose", 25.0, 30)
    initial_height = plant.height
    print("=== Garden Plant Growth ===")
    plant.show()
    for i in range(1,8):
        print(f"=== Day {i} ===")
        plant.grow(0.8)
        plant.age(1)
        plant.show()
    weekly_growth = plant.height - initial_height
    print(f"Growth this week: {weekly_growth:.1f}cm")
