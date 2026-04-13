class Plant:
    def __init__(self, name: str, height: float, age: int, grow_plant=0):
        self.name = name
        self.height = round(height, 1)
        self.days = age
        self.grow_plant = grow_plant

    def grow(self):
        self.height += self.grow_plant

    def age(self):
        self.days += 1

    def show(self):
        return f"Created: {self.name}: {self.height} cm, {self.days} days"


def main():
    raw_data = [
        ("Rose", 25.0, 30, 0),
        ("Oak", 200.0, 365, 0),
        ("Cactus", 5.0, 90, 0),
        ("Sunflower", 80.0, 45, 0),
        ("Fern", 15.0, 120, 0)
    ]

    garden = []
    for data in raw_data:
        name, height, age, grow = data
        garden.append(Plant(name, height, age, grow))

    print("=== Plant Factory Output ===")

    for plant in garden:
        print(plant.show())


if __name__ == "__main__":
    main()
