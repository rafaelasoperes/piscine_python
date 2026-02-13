class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
       
        self.initial_height = height

    def grow(self, cm):
        self.height += cm

    def age_one_day(self):
        self.age += 1

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"

def main():
    rose = Plant("Rose", 25, 30)

    print("=== Day 1 ===")
    print(rose.get_info())

    for _ in range(6):
        rose.grow(1)
        rose.age_one_day() 

    print("=== Day 7 ===")
    print(rose.get_info())

    growth_total = rose.height - rose.initial_height
    print(f"Growth this week: +{growth_total}cm")

if __name__ == "__main__":
    main()