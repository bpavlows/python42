#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(
            f"Plant created: {self.name}: {self.get_height():,.1f}cm,"
            f"{self.get_age()} days old"
        )

    def set_height(self, value: float) -> None:
        if (value <= 0):
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self.height = value
            print(f"Height updated: {self.height:,.1f}cm")

    def set_age(self, value: int) -> None:
        if (value <= 0):
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self.age = value
            print(f"Age updated: {self.age}cm")

    def get_height(self) -> float:
        return (self.height)

    def get_age(self) -> int:
        return (self.age)


def main() -> None:
    p1 = Plant("Rose", 15.0, 10)

    print("=== Garden Security System ===")
    p1.show()
    print()
    p1.set_height(25.0)
    p1.set_age(30)
    print()
    p1.set_height(-5)
    p1.set_age(-5)
    print()
    print(
        f"Current state: {p1.name}: {p1.get_height():,.1f}cm,"
        f"{p1.get_age()} days old"
    )


if __name__ == "__main__":
    main()
