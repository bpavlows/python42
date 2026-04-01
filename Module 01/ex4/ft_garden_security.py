#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"Plant created: {self.name}: {self.height:,.1f}cm, {self.age} days old")
    
    def set_height(self, value: float) -> None:
        if (value <= 0):
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            print(f"Height updated: {self.height:,.1f}cm")
            self.height = value
    
    def set_age(self, value: int) -> None:
        if (value <= 0):
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            print(f"Age updated: {self.age}cm")
            self.age = value


def main() -> None:
    p1 = Plant("Rose", 15.0, 10)

    print("=== Garden Security System ===")
    p1.show()
    print()
    p1.set_height(25.0);
    p1.set_age(30)
    print()
    p1.set_
    Rose: Error, height can't be negative
Height update rejected
Rose: Error, age can't be negative
Age update rejected
Current state: Rose: 25.0cm, 30 days old


    """
    get_height(), get_age()


Height updated: 25cm
Age updated: 30 days

Rose: Error, height can't be negative
Height update rejected
Rose: Error, age can't be negative
Age update rejected

Current state: Rose: 25.0cm, 30 days old
    """