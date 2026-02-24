class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__( name, height, age)
        self.color = color

    def bloom(self):
        print(f"{name} is blooming beautifully!")

class Tree(Plant):
    def __init__(self, name, height, age, trunk):
        super().__init__(name, height, age)
        self.trunk

    def produce_shade(self):
        print(f"")

class Vegetable(Plant): 
    def __init__(self, name, height, age, harvest, nutritional)
        super().__init__(name, height, age)
        self.harvest
        self.nutritional

def main():
    print("=== Garden Plant Types ===")

    rose = Flower("Rose", 25, 30, "red")

    oak = 