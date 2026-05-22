#!/usr/bin/env python3
import sys


def transform_data(data: list) -> None:
    print("\nTransform data:")
    print("---\n")
    for line in data:
        print(line + "#")
    print("\n---")
    new_filename = input("Enter new file name (or empty to skip): ").strip()
    if new_filename:
        file_handle = open(new_filename, 'w')
        for line in data:
            file_handle.write(line + "#\n")
        file_handle.close()
        print(f"Saving data to '{new_filename}'")
        print(f"Data saved in file '{new_filename}'.")
    else:
        print("Not saving data.")


def recover_ancient_text(filename: str) -> None:
    print("===  Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    file_handle = open(filename, 'r')
    content = file_handle.read()
    readed = []

    print("---\n")
    for line in content.strip().split('\n'):
        print(line)
        readed.append(line)
    print("\n---")

    file_handle.close()
    print(f"File '{filename}' closed.")
    transform_data(readed)


def main() -> None:
    if len(sys.argv) == 1:
        print("Usage: ft_archive_creation.py <file>")
        sys.exit(1)
    try:
        recover_ancient_text(sys.argv[1])
    except FileNotFoundError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")


if __name__ == "__main__":
    main()
