#!/usr/bin/env python3

class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_count: int = 0
            self._age_count: int = 0
            self._show_count: int = 0
            self._shade_count: int | None = None

        def display(self) -> None:
            print(
                f"Stats: {self._grow_count} grow, "
                f"{self._age_count} age, "
                f"{self._show_count} show."
            )
            if self._shade_count is not None:
                print(f" {self._shade_count} shade")

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        self._stats = self.Stats()

    @staticmethod
    def year_old(num: int) -> bool:
        return num > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def show(self) -> None:
        self._stats._show_count += 1
        print(
            f"{self.name.capitalize()}: {self.height:,.1f}cm,"
            f" {self.age} days old"
        )


class Flower(Plant):
    def __init__(
        self, name: str, height: float, age: int,
        color: str, _bloomed: bool = False
    ) -> None:
        super().__init__(name, height, age)
        self.color = color
        self._bloomed = _bloomed

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color.lower()}")
        if (self._bloomed):
            print(f" {self.name.capitalize()} is blooming beautifully!")
        else:
            print(f" {self.name.capitalize()} has not bloomed yet")

    def bloom(self) -> None:
        self._bloomed = True

    def grow(self, num: float) -> None:
        self._stats._grow_count += 1
        self.height += num

    def ages(self, num: int) -> None:
        self._stats._age_count += 1
        self.age += num


class Seed(Flower):
    def __init__(
        self, name: str, height: float, age: int,
        color: str, num_seeds: int
    ) -> None:
        super().__init__(name, height, age, color)
        self.num_seeds = num_seeds

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.num_seeds if self._bloomed else 0}")

    def bloom(self) -> None:
        super().bloom()
        self.num_seeds = 42


class Tree(Plant):
    def __init__(
        self, name: str, height: float, age: int,
        trunk_diameter: float, produce_shade: int
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.produce_shade = produce_shade
        self._stats._shade_count = 0

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:,.1f}cm")

    def produce_shades(self) -> None:
        print(f"[asking the {self.name.lower()} to produce shade]")
        print(
            f"Tree {self.name} now produces a shade of {self.height}"
            f"cm long and {self.trunk_diameter}cm wide."
        )
        if self._stats._shade_count is not None:
            self._stats._shade_count += 1


def display_plant_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.name.capitalize()}]")
    plant._stats.display()


def main() -> None:
    d1, d2 = 30, 400

    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is {d1} days more than a year? -> {Plant.year_old(d1)}")
    print(f"Is {d2} days more than a year? -> {Plant.year_old(d2)}")
    print()

    print("=== Flower")
    f1 = Flower("Rose", 15.0, 10, "red", False)
    f1.show()
    display_plant_stats(f1)
    f1.bloom()
    f1.grow(8)
    print(f"[asking the {f1.name.lower()} to grow and bloom]")
    f1.show()
    display_plant_stats(f1)

    print()
    print("=== Tree")
    t1 = Tree("Oak", 200.0, 365, 5.0, 0)
    t1.show()
    display_plant_stats(t1)
    t1.produce_shades()
    display_plant_stats(t1)

    print()
    print("=== Seed")
    s1 = Seed("Sunflower", 80.0, 45, "yellow", 0)
    s1.show()
    print(f"[make {s1.name.lower()} grow, age and bloom]")
    s1.bloom()
    s1.grow(30.0)
    s1.ages(20)
    s1.show()
    display_plant_stats(s1)

    print()
    print("=== Anonymous")
    a1 = Plant.create_anonymous()
    a1.show()
    display_plant_stats(a1)


if __name__ == "__main__":
    main()
