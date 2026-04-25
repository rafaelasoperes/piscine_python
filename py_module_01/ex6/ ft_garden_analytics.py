class Plant:
    class Stats:
        def __init__(self) -> None:
            self.grow_count: int = 0
            self.age_count: int = 0
            self.show_count: int = 0

        def display(self):
            print(f"Stats: {self.grow_count} grow, {self.age_count} age, "
                  f"{self.show_count} show")

    def __init__(self, name: str, height: float, age: int):
        self.name: str = name
        self.height: float = round(height, 1)
        self.age: int = age
        self.stats = self.Stats()

    @staticmethod
    def is_older_than_year(days):
        return days > 365

    @classmethod
    def create_anonymous(cls):
        return cls("Unknown plant", 0.0, 0)

    def show(self):
        self.stats.show_count += 1
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self, value):
        self.stats.grow_count += 1
        self.height += value

    def update_age(self, days):
        self.stats.age_count += 1
        self.age += days


class Flower(Plant):
    def __init__(self, name, height, age, color) -> None:
        super().__init__(name, height, age)
        self.color: str = color
        self.isValid: bool = False

    def bloom(self):
        self.isValid = True

    def show(self):
        super().show()
        print(f" Color: {self.color}")
        if self.isValid:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):
    class TreeStats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self.shade_count: int = 0

        def display(self):
            super().display()
            print(f" {self.shade_count} shade")

    def __init__(self, name, height, age, trunk) -> None:
        super().__init__(name, height, age)
        self.trunk: float = round(trunk, 1)
        self.stats = self.TreeStats()

    def produce_shade(self):
        self.stats.shade_count += 1
        print(f"Tree {self.name} now produces a shade of {self.height}cm "
              f"long and {self.trunk}cm wide.")

    def show(self):
        super().show()
        print(f" Trunk diameter: {self.trunk}cm")


class Seed(Flower):
    def __init__(self, name, height, age, color) -> None:
        super().__init__(name, height, age, color)
        self.seeds: int = 0
        self.isValid: bool = False

    def bloom(self):
        self.isValid = True
        self.seeds = 42

    def show(self):
        super().show()
        print(f" Seeds: {self.seeds}")


def display_any_plant_stats(plant):
    print(f"[statistics for {plant.name}]")
    plant.stats.display()


def main():
    print("=== Garden statistics ===")

    print("=== Check year-old")
    dia1 = 30
    dia2 = 400
    print(f"Is {dia1} days more than a year? -> "
          f"{Plant.is_older_than_year(dia1)}")
    print(f"Is {dia2} days more than a year? -> "
          f"{Plant.is_older_than_year(dia2)}")
    print()

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_any_plant_stats(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    rose.show()
    display_any_plant_stats(rose)
    print()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_any_plant_stats(oak)

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_any_plant_stats(oak)
    print()

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()

    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30)
    sunflower.update_age(20)
    sunflower.bloom()
    sunflower.show()
    display_any_plant_stats(sunflower)
    print()

    print("=== Anonymous")
    anon = Plant.create_anonymous()
    anon.show()
    display_any_plant_stats(anon)


if __name__ == "__main__":
    main()
