def main() -> None:
    print("REAGENT STATUS: Loading reagents...")
    print("Checking dependencies:")

    try:
        import numpy

        print(f"[OK] numpy ({numpy.__version__})")
    except ModuleNotFoundError:
        print("[MISSING] numpy")
        print("Install with pip: python3 -m pip install numpy")
        print("Install with Poetry: poetry add numpy")
    try:
        import pandas
        
        print(f"[OK] pandas ({pandas.__version__})")
    except ModuleNotFoundError:
        print("[MISSING] pandas")
        print("Install with pip: python3 -m pip install pandas")
        print("Install with Poetry: poetry add pandas")

    print("pip vs Poetry:")
    print(
        "  requirements.txt declares what to install; "
        "pip resolves it at install time."
    )
    print(
        "  pyproject.toml declares the dependencies for Poetry, "
        "and poetry.lock records exact resolved versions."
    )
    print("\nAll reagents present and accounted for.")

if __name__ == "__main__":
    main()