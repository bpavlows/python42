#!/usr/bin/env python3
import math


def get_player_pos() -> None:
    while True:
        inp1 = input("Enter new coordinates as floats in format 'x,y,z': ")
        try:
            inp = inp1.split(',')
            if len(inp) != 3:
                print("Invalid syntax")
                continue
            x = float(inp[0].strip())
            y = float(inp[1].strip())
            z = float(inp[2].strip())
            return(x, y, z)
        except ValueError as e:
            wrong = str(e).split("'")
            print(f"Error on parameter '{wrong[1]}': {e}")


def main() -> None:
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    p1 = get_player_pos()
    print(f"Got a first tuple: {p1}")
    print(f"It includes: X={p1[0]}, Y={p1[1]}, Z={p1[2]}")
    distance = math.sqrt(p1[0]**2 + p1[1]**2 + p1[2]**2)
    print(f"Distance to center: {distance:,.5}")
    print()
    print("Get a second set of coordinates")
    p2 = get_player_pos()
    distance2 = ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2)
    print(f"Distance between the 2 sets of coordinates: {distance2}")


if __name__ == "__main__":
    main()
