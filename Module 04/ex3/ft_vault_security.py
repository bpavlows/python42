#!/usr/bin/env python3


def secure_archive(
        filename: str, action: str = 'read', content: str = ''
        ) -> tuple:
    try:
        if action == 'read':
            with open(filename, 'r') as file_handle:
                file_content = file_handle.read()
            return (True, file_content)
        elif action == 'write':
            with open(filename, 'w') as file_handle:
                file_handle.write(content)
            return (True, 'Content successfully written to file')
    except Exception as e:
        return (False, str(e))
    return (False, 'Invalid action specified')


def main() -> None:
    print("=== Cyber Archives Security ===")
    print()
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive('/not/existing/file', 'read'))
    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive('/etc/master.passwd', 'read'))
    print()
    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive('ancient_fragment.txt', 'read'))
    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive('sample.txt', 'write', 'Hello, World!'))


if __name__ == "__main__":
    main()
