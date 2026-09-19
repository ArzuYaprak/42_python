class Plant:
    def __init__(self, name: str, height: float, age_days: int) -> None:
        self._name = name
        self._height = 0.0
        self._age_days = 0
        
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
        else:
            self._height = height

        if age_days < 0:
            print(f"{self._name}: Error, age can't be negative")
        else:
            self._age_days = age_days
        
    def show(self) -> None:
            print(f"{self._name}: {round(self._height, 1)}cm, {self._age_days} days old")
            
    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = height
        print(f"Height updated: {height:.0f}cm")

    def set_age(self, age_days: int) -> None:
        if age_days < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age_days = age_days
        print(f"Age updated: {self._age_days} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age_days

    def grow(self, growth: float) -> None:
        self.set_height(self._height + growth)

    def age(self, day: int) -> None:
        self.set_age(self._age_days + day)
        
class Flower(Plant):
    def __init__(self, name: str, height: float, age_days: int, color: str) -> None:
        self._name = name
        self._height = height
        self._age_days = age_days
        super().__init__(name, height, age_days)
        self._color = color
        self._bloomed = False
        
    def bloom(self) -> None:
        self._bloomed = True
        
    def show(self) -> None:
        super().show()
        print(f"Color {self._color}")
        if self._bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")
            
            
class Tree(Plant):
    def __init__(self, name: str, height: float, age_days: int, trunk_diameter: float):
        super().__init__(name, height, age_days)   
        self._trunk_diameter = trunk_diameter   
        
    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {round(self._trunk_diameter, 1)}cm")

    def produce_shade(self) -> None:
        print(
            f"Tree {self._name} now produces a shade of "
            f"{round(self._height, 1)}cm long and "
            f"{round(self._trunk_diameter, 1)}cm wide."
        )
class Vegetable(Plant):
    def __init__(self, name: str, height: float, age_days: int, harvest_season: str, nutritional_value: int):
        super().__init__(name, height, age_days)
        self._harvest_season = harvest_season
        self._nutritional_value = 0
        
    def age(self, days: int = 1) -> None:
        super().age(days)
        self._nutritional_value = self._nutritional_value + days

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")
    
if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print()
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April", 2.1)
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    tomato.grow(20)
    tomato.age(20)
    tomato.show()