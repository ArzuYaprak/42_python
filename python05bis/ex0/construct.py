import os
import sys
import site


def main() -> None:
    
    in_virtual_env: bool = sys.prefix != sys.base_prefix
    if in_virtual_env:
        environment_name: str = os.path.basename(sys.prefix)
        print("LABORATORY STATUS: The laboratory is sealed")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {environment_name}")
        print(f"Environment Path: {sys.prefix}")
        print("SUCCESS: You are working in an isolated environment!")
        print("Reagent installation path:")

        for package_path in site.getsitepackages():
            print(package_path)
    else:
        print("LABORATORY STATUS: You are working in the open")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print("WARNING: You are in the global environment!")
        print("To seal the laboratory, run:")
        print("python3 -m venv lab_env")
        print("source lab_env/bin/activate")
        print("Then run this program again.")
        print("Global environment package locations:")
        
        for package_path in site.getsitepackages():
            print(package_path)
    
if __name__ == "__main__":
    main()