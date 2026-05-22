#!/usr/bin/env python3
import sys


def transform_data(data: list) -> None:
    print("\nTransform data:")
    print("---\n")
    for line in data:
        print(line + "#")
    print("\n---")
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_filename = sys.stdin.readline().strip()
    if new_filename:
        print(f"Saving data to '{new_filename}'")
        try:
            file_handle = open(new_filename, 'w')
            for line in data:
                file_handle.write(line + "#\n")
            file_handle.close()
            print(f"Data saved in file '{new_filename}'.")
        except (PermissionError, FileNotFoundError) as e:
            print(
                f"[STDERR] Error opening file '{new_filename}': {e}",
                file=sys.stderr
            )
            print("Data not saved")
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
    except (FileNotFoundError, PermissionError) as e:
        print(
            f"[STDERR] Error opening file '{sys.argv[1]}': {e}",
            file=sys.stderr
        )


if __name__ == "__main__":
    main()
