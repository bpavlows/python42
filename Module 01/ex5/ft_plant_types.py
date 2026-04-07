#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.blooming = False

    def bloom(self) -> None:
        self.blooming = True
        print(f"[asking the {self.name.lower()} to bloom]")

    def show(self) -> None:
        print(
            f"{self.name}: {self.height:,.1f}cm, {self.age} days old\n"
            f" Color: {self.color}"
        )
        if (self.blooming):
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.producing_shade = False

    def produce_shade(self) -> None:
        self.producing_shade = True
        print(f"[asking the {self.name.lower()} to produce shade]")
        print(
                f"Tree {self.name} now produces a shade of "
                f"{self.height:,.1f}cm long and "
                f"{self.trunk_diameter:,.1f}cm wide."
            )

    def show(self) -> None:
        print(
            f"{self.name}: {self.height:,.1f}cm, {self.age} days old\n"
            f" Trunk diameter: {self.trunk_diameter:,.1f}cm"
        )


class Vegetable(Plant):
    def __init__(
        self, name: str, height: float, age: int,
        harvest_season: str, nutritional_value: int
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        print(
            f"{self.name}: {self.height:,.1f}cm, {self.age} days old\n"
            f" Harvest season: {self.harvest_season}\n"
            f" Nutritional value: {self.nutritional_value}"
        )

    def grow_and_age(self, days) -> None:
        print(f"[make {self.name.lower()} grow and age for {days} days]")
        for day in range(days):
            self.height += 2.1
            self.age += 1
            self.nutritional_value += 1


def main() -> None:
    f1 = Flower("Rose", 15.0, 10, "red")
    t1 = Tree("Oak", 200.0, 365, 5.0)
    v1 = Vegetable("Tomato", 5.0, 10, "April", 0)

    print("=== Garden Plant Types ===")
    print("=== Flower")
    f1.show()
    f1.bloom()
    f1.show()
    print()

    print("=== Tree")
    t1.show()
    t1.produce_shade()
    print()

    print("=== Vegetable")
    v1.show()
    v1.grow_and_age(20)
    v1.show()


if __name__ == "__main__":
    main()
