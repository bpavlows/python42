#!/usr/bin/env python3
import random


def gen_player_achievements(all_achievements) -> set:
    count = random.randint(5, 10)
    selected = random.sample(all_achievements, count)
    return set(selected)


def main() -> None:
    master_list = {
        'Crafting Genius', 'World Savior', 'Master Explorer',
        'Collector Supreme', 'Untouchable', 'Boss Slayer', 'Strategist',
        'Unstoppable', 'Speed Runner', 'Survivor', 'Treasure Hunter',
        'First Steps', 'Sharp Mind', 'Hidden Path Finder'
    }
    alice = gen_player_achievements(list(master_list))
    bob = gen_player_achievements(list(master_list))
    charlie = gen_player_achievements(list(master_list))
    dylan = gen_player_achievements(list(master_list))
    print("=== Achievement Tracker System ===")
    print()
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    print()
    print(
        f"All distinct achievements: {set.union(alice, bob, charlie, dylan)}"
        )
    print()
    print(
        f"Common achievements: {set.intersection(alice, bob, charlie, dylan)}"
    )
    print()
    print(
        f"Only Alice has: {alice.difference(set.union(bob, charlie, dylan))}"
    )
    print(
        f"Only Bob has: {bob.difference(set.union(alice, charlie, dylan))}"
    )
    print(
        f"Only Charlie has: {charlie.difference(set.union(alice, bob, dylan))}"
    )
    print(
        f"Only Dylan has: {dylan.difference(set.union(alice, bob, charlie))}"
    )
    print()
    print(f"Alice is missing: {master_list.difference(alice)}")
    print(f"Bob is missing: {master_list.difference(bob)}")
    print(f"Charlie is missing: {master_list.difference(charlie)}")
    print(f"Dylan is missing: {master_list.difference(dylan)}")


if __name__ == "__main__":
    main()
