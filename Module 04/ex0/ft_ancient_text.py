#!/usr/bin/env python3
import sys


def recover_ancient_text(filename: str) -> None:
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")
    try:
        file_handle = open(filename, 'r')
        content = file_handle.read()
        print("---\n")
        for line in content.strip().split('\n'):
            print(line)
        print("\n---")
        file_handle.close()
        print(f"File '{filename}' closed.")
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")


def main() -> None:
    if len(sys.argv) == 1:
        print("Usage: ft_ancient_text.py <file>")
        sys.exit(1)
    recover_ancient_text(sys.argv[1])


if __name__ == "__main__":
    main()
