class Plant:
    def __init__(self, name, height, days, grow_plant):
        self.name = name
        self.height = height
        self.days = days
        self.grow_plant = grow_plant
        self.initial_height = height

    def grow(self):
        self.height += self.grow_plant

    def age(self):
        self.days += 1

    def get_info(self):
        return f"{self.name}: {round(self.height, 1)} cm, {self.days} days old"


def main():
    rose = Plant("Rose", 25, 30, 0.8)

    print("=== Garden Plant Growth ===")
    print(rose.get_info())

    for day in range(1, 8):
        rose.grow()
        rose.age()
        print(f"=== Day {day} ===")
        print(rose.get_info())

    growth_total = round(rose.height - rose.initial_height, 1)
    print(f"Growth this week: {growth_total}cm")


if __name__ == "__main__":
    main()
