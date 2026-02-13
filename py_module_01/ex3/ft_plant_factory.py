class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_status(self):
        return f"Created: {self.name} ({self.height}cm, {self.age} days)"

def main():
    raw_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]

    garden = []
    for i in range(len(raw_data)):
        name, height, age = raw_data[i]
        garden.append(Plant(name, height, age))

    print("=== Plant Factory Output ===")
    
    for i in range(len(garden)):
        print(garden[i].get_status())

    print("\n")
    print(f"Total plants created: {len(garden)}")

if __name__ == "__main__":
    main()