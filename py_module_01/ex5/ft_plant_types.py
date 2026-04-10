class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.days = age

    def grow(self, value):
        self.height = round(self.height + value, 1)

    def age(self):
        self.days += 1

    def show(self):
        print(f"{self.name.capitalize()}:"
              "{self.height}cm, {self.days} days old")


class Flower(Plant):
    def __init__(self, name, height, age, color, isValid):
        super().__init__(name, height, age)
        self.color = color
        self.isValid = isValid

    def bloom(self):
        super().show()
        print(f" Color: {self.color}")
        if (self.isValid is True):
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")
            print(f"[asking the {self.name} to bloom]")


class Tree(Plant):
    def __init__(self, name, height, age, trunk):
        super().__init__(name, height, age)
        self.trunk_diameter = round(trunk, 1)

    def produce_shade(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")
        print(f"[asking the {self.name} to produce shade]")
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.height}cm long and {self.trunk_diameter}cm wide."
        )


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
        super().show()
        print(f"Harvest season: {self.harvest}")
        print(f"Nutritional value: {self._nutritional}")


def main():
    print("=== Garden Plant Types ===")
    print()
    print("=== Flower")
    flower1 = Flower("Rose", 15.0, 30, "red", False)
    flower1.bloom()

    flower = Flower("Rose", 15.0, 30, "red", True)
    flower.bloom()

    print()
    print("=== Tree")
    tree = Tree("Oak", 200.0, 365, 5.0)
    tree.produce_shade()

    print()
    print("=== Vegetable")
    vegetable1 = Vegetable("tomato", 5.0, 10, "April")
    vegetable1.nutricional()

    vegetable = Vegetable("tomato", 5.0, 10, "April")
    vegetable.set_nutritional(20)
    vegetable.nutricional()


if __name__ == "__main__":
    main()
