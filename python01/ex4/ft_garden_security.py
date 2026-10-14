class Plant:
    # not: Alt çizgili alanlar doğrudan dışarıdan değiştirilmesin diye korunuyor.
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
        # not: Değeri değiştirmeden önce negatif yükseklik kontrol ediliyor.
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
        # not: Dışarıdan değeri okumak için getter kullanılıyor.
        return self._height

    def get_age(self) -> int:
        return self._age_days

    def grow(self, growth: float) -> None:
        self.set_height(self._height + growth)

    def age(self, day: int) -> None:
        self.set_age(self._age_days + day)
        
if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()
    print()
    rose.set_height(25.0)
    rose.set_age(30)
    print()
    rose.set_height(-10.0)
    rose.set_age(-3)
    print()
    print("Current state: ", end="")
    rose.show()
