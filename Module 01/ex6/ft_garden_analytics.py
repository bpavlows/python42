#!/usr/bin/env python3

class Plant:
	class Stats:
		def __init__(self) -> None:
			self._grow_count: int = 0
			self._age_count: int = 0
			self._show_count: int = 0
		
		def display(self) -> None:
			print(f"[statistics for {self.name.capitalize()}]")
			self._show_count += 1
			print(
				f"Stats: {self._grow_count} grow, "
				f"{self._age_count} age, "
				f"{self._show_count} show."
			)

	def __init__(self, name, height, age) -> None:
		self.name = name
		self.height = height
		self.age = age
		self._stats = self.Stats()
	
	@staticmethod
	def year_old(num: int) -> bool:
		return num > 365


class Flower(Plant):
	def __init__(self, name, height, age, color, _bloomed: False) -> None:
		super().__init__(name, height, age)
		self.color = color
		self._bloomed = _bloomed

	def show(self):
		print(f"{self.name}: {self.height}cm, {self.age} days old")
		print(f" Color: {self.color.lower()}")
		if (self._bloomed):
			print(f" {self.name.capitalize()} is blooming beautifully!")
		else:
			print(f" {self.name.capitalize()} has not bloomed yet")

	def bloom(self) -> None:
		self._bloomed = True

	def grow(self, num) -> None:
		self._grow_count += 1
		self.height += num

	def age(self, num) -> None:
		self._age_count += 1
		self.age += num


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
	Plant.Stats.display(f1)
	f1.bloom()
	f1.grow(8)
	print(f"[asking the {f1.name.lower()} to grow and bloom]")
	f1.show()
	f1.display()


if __name__ == "__main__":
	main()
