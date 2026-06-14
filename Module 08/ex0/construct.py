import sys
import os
import site


def is_virtual_environment() -> bool:
    return sys.prefix != sys.base_prefix


def outside_venv() -> None:
    print("Current Python: ", end="")
    print(sys.executable)
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print()
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate # On Windows")
    print()
    print("Then run this program again.")


def inside_venv() -> None:
    venv_name = os.path.basename(sys.prefix)
    print("Current Python: ", end="")
    print(sys.executable)
    print(f"Virtual Environment: {venv_name}")
    print("Environment Path: ", end="")
    print(sys.prefix)
    print()
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print()
    print("Package installation path:")
    packages = site.getsitepackages()
    if packages:
        print(packages[0])


def main() -> None:
    print()
    print("MATRIX STATUS: ", end="")

    if is_virtual_environment():
        print("Welcome to the construct\n")
        inside_venv()
    else:
        print("You're still plugged in\n")
        outside_venv()


if __name__ == "__main__":
    main()
