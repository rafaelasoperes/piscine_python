class Plant:
    def __init__(self, name: str, heigth: float, age: int):
        self.name: str = name
        self.height: float = heigth
        self.days: int = age

    def grow(self, value):
        self.height = round(self.height + value, 1)

    def age(self):
        self.days += 1

    def show(self):
        print(f"{self.name.capitalize()}:"
              f"{self.height}cm, {self.days} days old")


class Flower(Plant):
    def __init__(self, name: str, heigth: float, age: int, color):
        super().__init__(name, heigth, age)
        self.color: str = color
        self.isValid: bool = False

    def bloom(self):
        self.isValid = True

    def show(self):
        super().show()
        print(f" Color: {self.color}")
        if (self.isValid is True):
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")
            print(f"[asking the {self.name} to bloom]")


class Tree(Plant):
    def __init__(self, name, height, age, trunk):
        super().__init__(name, height, age)
        self.trunk_diameter = round(trunk, 1)

    def produce_shade(self):
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.height}cm long and {self.trunk_diameter}cm wide."
        )

    def show(self):
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")
        print(f"[asking the {self.name} to produce shade]")


class Vegetable(Plant):
    def __init__(self, name, height, day, harvest, nutritional=0):
        super().__init__(name, height, day)
        self.harvest = harvest
        self._nutritional = nutritional

    def get_nutritional(self):
        return self._nutritional

    def set_nutritional(self, value):
        print(f"[make {self.name} grow and age for {value} days]")
        i = 0
        while i < value:
            super().age()
            super().grow(2.1)
            i += 1
        self._nutritional = value

    def nutricional(self):
        print(f" Nutritional value: {self._nutritional}")

    def show(self):
        super().show()
        print(f" Harvest season: {self.harvest}")
        self.nutricional()


def main():
    print("=== Garden Plant Types ===")
    print()
    print("=== Flower")
    flower = Flower("Rose", 15.0, 30, "red")
    flower.show()

    flower.bloom()
    flower.show()

    print()
    print("=== Tree")
    tree = Tree("Oak", 200.0, 365, 5.0)
    tree.show()
    tree.produce_shade()

    print()
    print("=== Vegetable")
    vegetable1 = Vegetable("tomato", 5.0, 10, "April")
    vegetable1.show()

    vegetable = Vegetable("tomato", 5.0, 10, "April")
    vegetable.set_nutritional(20)
    vegetable.show()


if __name__ == "__main__":
    main()
