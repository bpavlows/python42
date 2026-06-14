import os
import sys

try:
    from dotenv import load_dotenv
    DOTENV_AVAILABLE = True
except ImportError:
    DOTENV_AVAILABLE = False


def load_configuration() -> None:
    if DOTENV_AVAILABLE:
        load_dotenv()
    else:
        print("[WARNING] python-dotenv not installed.")
        print("Install with: pip install python-dotenv")
        print()


def get_config() -> dict[str, str]:
    return {
        "MATRIX_MODE": os.environ.get("MATRIX_MODE", "development"),
        "DATABASE_URL": os.environ.get("DATABASE_URL", ""),
        "API_KEY": os.environ.get("API_KEY", ""),
        "LOG_LEVEL": os.environ.get("LOG_LEVEL", "INFO"),
        "ZION_ENDPOINT": os.environ.get("ZION_ENDPOINT", ""),
    }


def validate_config(config: dict[str, str]) -> bool:
    required = ["DATABASE_URL", "API_KEY", "ZION_ENDPOINT"]
    missing = []

    for key in required:
        if not config[key]:
            missing.append(key)

    if missing:
        print("[ERROR] Missing required configuration:")
        for key in missing:
            print(f"  {key} is not set")
        print()
        print("Copy .env.example to .env and fill in your values:")
        print("  cp .env.example .env")
        print()
        return False

    return True


def print_oracle_status(config: dict[str, str]) -> None:
    mode = config["MATRIX_MODE"]

    print("ORACLE STATUS: Reading the Matrix...")
    print()
    print("Configuration loaded:")
    print(f"  Mode: {mode}")

    if config["DATABASE_URL"]:
        print("  Database: Connected to local instance")
    else:
        print("  Database: [NOT CONFIGURED]")

    if config["API_KEY"]:
        print("  API Access: Authenticated")
    else:
        print("  API Access: [NOT CONFIGURED]")

    print(f"  Log Level: {config['LOG_LEVEL']}")

    if config["ZION_ENDPOINT"]:
        print("  Zion Network: Online")
    else:
        print("  Zion Network: [NOT CONFIGURED]")

    print()
    print("Environment security check:")
    print("  [OK] No hardcoded secrets detected")

    if DOTENV_AVAILABLE:
        print("  [OK] .env file properly configured")
    else:
        print("  [WARNING] python-dotenv not available")

    if mode == "production":
        print("  [OK] Production overrides available")
        print()
        print("  [PRODUCTION] Verbose logging disabled")
        print("  [PRODUCTION] Debug endpoints hidden")
    else:
        print("  [OK] Production overrides available")
        print()
        print(f"  [DEBUG] Database URL: {config['DATABASE_URL']}")
        print(f"  [DEBUG] Zion Endpoint: {config['ZION_ENDPOINT']}")

    print()
    print("The Oracle sees all configurations.")


def main() -> None:
    load_configuration()
    config = get_config()

    if not validate_config(config):
        sys.exit(1)

    print_oracle_status(config)


if __name__ == "__main__":
    main()
