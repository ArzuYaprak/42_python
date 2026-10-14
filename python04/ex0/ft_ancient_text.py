import typing
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery ===")
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
 # not: Dosya işlemlerinde with kullanmak dosyanın güvenli biçimde kapanmasını sağlar.
