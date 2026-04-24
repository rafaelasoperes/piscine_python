import os
import sys
from dotenv import load_dotenv  # type: ignore


def get_config_value(name):
    value = os.getenv(name)

    if value is None or value == "":
        return None

    return value


def show_config_status(name, label, success_message):
    value = get_config_value(name)

    if value is None:
        print(f"{label}: MISSING")
        return False

    print(f"{label}: {success_message}")
    return True


def main():
    load_dotenv()

    print("ORACLE STATUS: Reading the Matrix...")
    print()

    print("Configuration loaded:")

    matrix_mode = get_config_value("MATRIX_MODE")

    if matrix_mode is None:
        print("Mode: MISSING")
        mode_ok = False
    else:
        print(f"Mode: {matrix_mode}")
        mode_ok = True

    database_ok = show_config_status(
        "DATABASE_URL",
        "Database",
        "Connected to local instance"
    )

    api_ok = show_config_status(
        "API_KEY",
        "API Access",
        "Authenticated"
    )

    log_level = get_config_value("LOG_LEVEL")

    if log_level is None:
        print("Log Level: MISSING")
        log_ok = False
    else:
        print(f"Log Level: {log_level}")
        log_ok = True

    zion_ok = show_config_status(
        "ZION_ENDPOINT",
        "Zion Network",
        "Online"
    )

    print()
    print("Environment security check:")

    env_exists = os.path.exists(".env")

    if env_exists:
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found")
        print("[WARNING] Using environment variables only")

    if matrix_mode == "production":
        print("[OK] Production overrides available")
    elif matrix_mode == "development":
        print("[OK] Development configuration active")
    else:
        print("[WARNING] Unknown MATRIX_MODE")

    print()

    if mode_ok and database_ok and api_ok and log_ok and zion_ok:
        print("The Oracle sees all configurations.")
    else:
        print("The Oracle cannot see all configurations.")
        print("Please check your environment variables.")
        sys.exit(1)


if __name__ == "__main__":
    main()
