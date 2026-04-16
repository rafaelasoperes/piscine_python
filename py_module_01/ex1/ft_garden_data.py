class Plant:
    def __init__(self, name: str, heigth: float, age: int):
        self.name: str = name
        self.heigth: float = heigth
        self.age: int = age

    def show(self):
        return f"{self.name}: {self.heigth}cm, {self.age} days old"


def main():
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    garden = [rose, sunflower, cactus]

    print("=== Garden Plant Registry ===")

    for i in garden:
        print(i.show())


if __name__ == "__main__":
    main()
