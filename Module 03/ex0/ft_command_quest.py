#!/usr/bin/env python3
import sys

def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    total = len(sys.argv)
    arg = 1
    if total > 1:
        for arg in sys.argv:
            print(f"Argument {arg}: {sys.argv[arg]}")
    else:
        print("No arguments provided!")
    print(f"Total arguments: {total}")

