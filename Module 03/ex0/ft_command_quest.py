#!/usr/bin/env python3
import sys


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    total: int = len(sys.argv)
    id: int = 1
    if total > 1:
        for arg in sys.argv[1:]:
            print(f"Argument {id}: {arg}")
            id += 1
    else:
        print("No arguments provided!")
    print(f"Total arguments: {total}")


if __name__ == "__main__":
    main()
