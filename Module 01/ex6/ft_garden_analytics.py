#!/usr/bin/env python3

class Plant:
	class Stats:
		def __init__(self) -> None:
			self._grow_count: int = 0
			self._age_count: int = 0
			self._show_count: int = 0
		
		def display(self) -> None:
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
	
	@classmethod
	def create_anonymous(cls) -> "Plant":
		return cls("Unknown plant", 0.0, 0)
	
	def show(self) -> None:
		self._stats._show_count += 1


class Flower(Plant):
	def __init__(self, name, height, age, color, _bloomed: bool = False) -> None:
		super().__init__(name, height, age)
		self.color = color
		self._bloomed = _bloomed

	def show(self):
		super().show()
		print(f"{self.name}: {self.height}cm, {self.age} days old")
		print(f" Color: {self.color.lower()}")
		if (self._bloomed):
			print(f" {self.name.capitalize()} is blooming beautifully!")
		else:
			print(f" {self.name.capitalize()} has not bloomed yet")

	def bloom(self) -> None:
		self._bloomed = True

	def grow(self, num) -> None:
		self._stats._grow_count += 1
		self.height += num

	def age(self, num) -> None:
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

class Tree(Plant):
	def __init__(
		self, name: str, height: float, age: int,
		trunk_diameter: float, produce_shade: int
	) -> None:
		super().__init__(name, height, age)
		self.trunk_diameter = trunk_diameter
		self.produce_shade = produce_shade
	
	def show(self) -> None:
		super().show()

	def produce_shade(self) -> None:
		self.produce_shade += 1


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



if __name__ == "__main__":
	main()
