import sys
import importlib

REQUIRED = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "matplotlib": "Visualization ready",
}


def check_dependencies() -> dict[str, tuple[bool, str]]:
    results = {}

    for package in REQUIRED:
        try:
            module = importlib.import_module(package)
            version = getattr(module, "__version__", "unknown")
            results[package] = (True, version)
        except ImportError:
            results[package] = (False, "")

    return results


def print_loading_status(status: dict[str, tuple[bool, str]]) -> None:
    print()
    print("LOADING STATUS: Loading programs...")
    print()
    print("Checking dependencies:")

    missing = False

    for package, description in REQUIRED.items():
        installed, version = status[package]

        if installed:
            print(f"[OK] {package} ({version}) - {description}")
        else:
            print(f"[MISSING] {package} - NOT FOUND")
            missing = True

    if missing:
        print()
        print("[ERROR] Missing required dependencies!")
        print()
        print("Install with pip:")
        print("pip install -r requirements.txt")
        print()
        print("Install with Poetry:")
        print("poetry install")
        print("poetry run python loading.py")
        sys.exit(1)

    print()


def generate_matrix_data(n: int = 1000):
    import numpy as np

    rng = np.random.default_rng(seed=42)

    time = np.arange(n)
    signal = rng.normal(loc=0.0, scale=1.0, size=n)

    return time, signal


def analyze_data(time, signal):
    import pandas as pd

    return pd.DataFrame(
        {
            "time": time,
            "signal_strength": signal,
        }
    )


def generate_visualization(df, output_path: str = "matrix_analysis.png") -> None:
    import matplotlib

    matplotlib.use("Agg")

    import matplotlib.pyplot as plt

    plt.figure(figsize=(8, 4))
    plt.plot(df["time"], df["signal_strength"])
    plt.title("Matrix Data Analysis")
    plt.xlabel("Time")
    plt.ylabel("Signal Strength")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def main() -> None:
    status = check_dependencies()
    print_loading_status(status)

    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")

    time, signal = generate_matrix_data()
    df = analyze_data(time, signal)

    print("Generating visualization...")

    output_file = "matrix_analysis.png"
    generate_visualization(df, output_file)

    print()
    print("Analysis complete!")
    print(f"Results saved to: {output_file}")


if __name__ == "__main__":
    main()
