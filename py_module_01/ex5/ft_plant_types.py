class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = round(height, 1)
        self.age = age

    def show(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"


class Flower(Plant):
    def __init__(self, name, height, age, color, isValid):
        super().__init__(name, height, age)
        self.color = color
        self.isValid = isValid

    def bloom(self):
        print(super().show())
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
        print(super().show())
        print(f"Trunk diameter: {self.trunk_diameter}cm")
        print(f"[asking the {self.name} to produce shade]")
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.height}cm long and {self.trunk_diameter}cm wide."
        )


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest, nutritional):
        super().__init__(name, height, age)
        self.harvest
        self.nutritional


def main():
    print("=== Garden Plant Types ===")
    print("\n")
    print("=== Flower")
    rose1 = Flower("Rose", 15.0, 30, "red", False)
    rose1.bloom()

    rose = Flower("Rose", 15.0, 30, "red", True)
    rose.bloom()

    print("\n")
    print("=== Tree")

    tree = Tree("Oak", 200.0, 365, 5.0)
    tree.produce_shade()


if __name__ == "__main__":
    main()
