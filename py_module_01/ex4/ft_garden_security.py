class SecurePlant:
    def __init__(self, name, height, age):
        self.name = name
        self._height = round(height, 1)
        self._age = age

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def set_height(self, value):
        if value < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")

        else:
            self._height = value
            print(f"Height updated: {value}cm")

    def set_age(self, value):
        if value < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")

        else:
            self._age = value
            print(f"Age updated: {value} days")


def main():
    print("=== Garden Security System ===")

    rose = SecurePlant("Rose", 15.0, 10)
    name = rose.name
    age = rose.get_age()
    height = rose.get_height()
    print(f"Plant created: {name}: {height:.1f}cm, {age} days old")
    print()

    rose.set_height(25)
    rose.set_age(30)
    print()

    rose.set_height(-5)
    rose.set_age(-5)
    newAge = rose.get_age()
    newHeight = rose.get_height()

    print()
    print(f"Current state: {name} : {newHeight:.1f}cm, {newAge} days old")


if __name__ == "__main__":
    main()
