class Plant:
    def __init__(self, name, heigth, age):
        self.name = name
        self.heigth = heigth
        self.age = age

    def info(self):
        print(f"{self.name}: {self.heigth}cm, {self.age} days old")
   
def main():
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    garden = [rose, sunflower, cactus]

    print("=== Garden Plant Registry ===")

    for i in range(len(garden)):
        garden[i].info()

if __name__ == "__main__":
    main()
