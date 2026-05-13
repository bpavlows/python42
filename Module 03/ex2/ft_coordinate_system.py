#!/usr/bin/env python3
import math


def calculate_distance(point_a, point_b) -> float:
    dx = point_b[0] - point_a[0]
    dy = point_b[1] - point_a[1]
    dz = point_b[2] - point_a[2]
    return math.sqrt(dx**2 + dy**2 + dz**2)


def get_player_pos() -> tuple:
    while True:
        line = input("Enter new coordinates as floats in format 'x,y,z': ")
        try:
            parts = line.split(',')
            if len(parts) != 3:
                print("Invalid syntax")
                continue
            coords = [float(p.strip()) for p in parts]
            return tuple(coords)
        except ValueError as e:
            err_msg = str(e).split(':')[-1].strip()
            print(f"Error on parameter {err_msg}: {e}")


def main() -> None:
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    p1 = get_player_pos()
    print(f"Got a first tuple: {p1}")
    print(f"It includes: X={p1[0]}, Y={p1[1]}, Z={p1[2]}")
    dist_center = calculate_distance(p1, (0.0, 0.0, 0.0))
    print(f"Distance to center: {dist_center:.4f}")
    print()
    print("Get a second set of coordinates")
    p2 = get_player_pos()
    dist_between = calculate_distance(p1, p2)
    print(f"Distance between the 2 sets of coordinates: {dist_between:.4f}")


if __name__ == "__main__":
    main()
