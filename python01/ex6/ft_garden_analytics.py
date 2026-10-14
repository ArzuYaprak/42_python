class Plant:
    # not: Bu sürüm davranış çağrılarını sayarak istatistik tutuyor.
    class Statistics:
        # not: İç sınıf Plant'in çağrı sayaçlarını yönetiyor.
        def __init__(self) -> None:
            self.__grow_calls = 0
            self.__age_calls = 0
            self.__show_calls = 0

        def add_grow(self) -> None:
            self.__grow_calls += 1

        def add_age(self) -> None:
            self.__age_calls += 1

        def add_show(self) -> None:
            self.__show_calls += 1

        def display(self) -> None:
            print(
                f"Stats: {self.__grow_calls} grow, "
                f"{self.__age_calls} age, "
                f"{self.__show_calls} show"
            )

    def __init__(self, name: str, height: float, age_days: int) -> None:
        self._name = name
        self._height = 0.0
        self._age_days = 0
        self._statistics = Plant.Statistics()
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
        else:
            self._height = height
        if age_days < 0:
            print(f"{self._name}: Error, age can't be negative")
        else:
            self._age_days = age_days

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            return
        self._height = height

    def set_age(self, age_days: int) -> None:
        if age_days < 0:
            print(f"{self._name}: Error, age can't be negative")
            return
        self._age_days = age_days

    def grow(self, growth: float) -> None:
        self.set_height(self._height + growth)
        self._statistics.add_grow()

    def age(self, days: int) -> None:
        self.set_age(self._age_days + days)
        self._statistics.add_age()

    def show(self) -> None:
        self._statistics.add_show()
        print(
            f"{self._name}: {round(self._height, 1)}cm, "
            f"{self._age_days} days old"
        )

    def display_statistics(self) -> None:
        self._statistics.display()

    @staticmethod
    def is_older_than_year(age_days: int) -> bool:
        # not: Bu işlem belirli bir nesneye ihtiyaç duymuyor.
        return age_days > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        # not: cls çağrıyı yapan sınıfı temsil ediyor.
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(
        self, name: str, height: float, age_days: int, color: str
    ) -> None:
        super().__init__(name, height, age_days)
        self._color = color
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._bloomed:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")


class Tree(Plant):
    class Statistics(Plant.Statistics):
        def __init__(self) -> None:
            super().__init__()
            self.__shade_calls = 0

        def add_shade(self) -> None:
            self.__shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f" {self.__shade_calls} shade")

    def __init__(
        self, name: str, height: float,
        age_days: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age_days)
        self._statistics = Tree.Statistics()
        self._trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {round(self._trunk_diameter, 1)}cm")

    def produce_shade(self) -> None:
        self._statistics.add_shade()
        print(
            f"Tree {self._name} now produces a shade of "
            f"{round(self._height, 1)}cm long and "
            f"{round(self._trunk_diameter, 1)}cm wide."
        )


class Seed(Flower):
    def __init__(
        self, name: str, height: float, age_days: int,
        color: str, seed_count: int
    ) -> None:
        super().__init__(name, height, age_days, color)
        self._seed_count = seed_count

    def show(self) -> None:
        super().show()
        if self._bloomed:
            print(f" Seeds: {self._seed_count}")
        else:
            print(" Seeds: 0")


def display_statistics(plant: Plant) -> None:
    plant.display_statistics()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[statistics for Rose]")
    display_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    display_statistics(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[statistics for Oak]")
    display_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    display_statistics(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow", 42)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    display_statistics(sunflower)

    print("\n=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    print("[statistics for Unknown plant]")
    display_statistics(anonymous)
