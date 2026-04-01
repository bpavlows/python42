#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, plant_age: int) -> None:
        self.name = name
        self.height = height
        self.plant_age = plant_age

    def show(self) -> None:
        message: str = (
            f"Created: {self.name}: "
            f"{self.height}cm, {self.plant_age} days old"
        )
        print(message)


def main() -> None:
    garden: list[Plant] = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120)
    ]

    print("=== Plant Factory Output ===")

    for plant in garden:
        plant.show()


if __name__ == "__main__":
    main()
