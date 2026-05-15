#!/usr/bin/env python3
import sys


def recover_ancient_text(filename: str) -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print(f"Accessing file '{filename}'")

    file_handle = open(filename, 'r')
    content = file_handle.read()

    print("---\n")
    for line in content.strip().split('\n'):
        print(line)
    print("\n---")

    file_handle.close()
    print(f"File '{filename}' closed.")


def main() -> None:
    if len(sys.argv) == 1:
        print("Usage: ft_ancient_text.py <file>")
        sys.exit(1)
    try:
        recover_ancient_text(sys.argv[1])
    except FileNotFoundError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")


if __name__ == "__main__":
    main()
