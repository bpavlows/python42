#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, plant_age: int) -> None:
        self.name = name
        self.height = height
        self.plant_age = plant_age

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.plant_age += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:,.1f}cm, {self.plant_age} days old")


def main() -> None:
    p1 = Plant("Rose", 25, 30)
    # p2 = Plant("Sunflower", 80, 45)
    # p3 = Plant("Cactus", 15, 120)

    print("=== Garden Plant Growth ===")
    x = range(1, 8, 1)
    initial_h = p1.height

    for i in x:
        print(f"=== Day {i} ===")
        p1.show()
        p1.grow()
        p1.age()

    week = round(p1.height - initial_h)
    print(f"Growth this week: {week}cm")


if __name__ == "__main__":
    main()
