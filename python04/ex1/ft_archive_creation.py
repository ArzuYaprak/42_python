import typing
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{sys.argv[1]}'")
        file_name = sys.argv[1]
        try:
            file: typing.IO[str] = open(file_name, "r")
            content: str = file.read()
            file.close()
        except OSError as error:
            print(f"Error opening file '{file_name}': {error}")
        else:
            print("---")
            print()
            print(content)
            print()
            print("---")
            print(f"File '{file_name}' closed.")
            print()
            transformed_content = ""

            for line in content.splitlines():
                transformed_content += line + "#\n"
            print("Transform data:")
            print("---")
            print()
            print(transformed_content)
            print("---")
            new_file_name = input("Enter new file name (or empty): ")
            if new_file_name == "":
                print("Not saving data.")
            else:
                print(f"Saving data to '{new_file_name}'")
                try:
                    new_file: typing.IO[str] = open(new_file_name, "w")
                    new_file.write(transformed_content)
                    new_file.close()
                except OSError as error:
                    print(f"Error opening file '{new_file_name}': {error}")
                else:
                    print(f"Data saved in file '{new_file_name}'.")
 # not: Arşiv oluştururken dosya yolu ve dosya modu sonucu doğrudan etkiler.
