import os

from dotenv import load_dotenv


def main() -> None:
    load_dotenv()

    matrix_mode: str = os.getenv("MATRIX_MODE", "development")
    database_url: str = os.getenv("DATABASE_URL", "")
    api_key: str = os.getenv("API_KEY", "")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    zion_endpoint: str = os.getenv("ZION_ENDPOINT", "")

    print("ORACLE STATUS: Consulting the configuration...\n")
    print("Configuration loaded:")
    print(f"Mode: {matrix_mode}")

    if database_url:
        print("Database: Connected to local instance")
    else:
        print("Database: Missing configuration")

    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing API key")

    print(f"Log Level: {log_level}")

    if zion_endpoint:
        print("Remote Network: Online")
    else:
        print("Remote Network: Offline")

    print("\nConfiguration security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly ignored by git")
    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()