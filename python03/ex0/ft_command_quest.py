import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    if len(sys.argv) < 2:
        print("No arguments provided!")
    else:
        i = 1
        print(f"Arguments received: {len(sys.argv) - 1}")
        while i <= len(sys.argv) - 1:
            print(f"Argument {i}: {sys.argv[i]}")
            i = i + 1
    print(f"Total arguments: {len(sys.argv)}")
        
 # not: Komut satırı argümanları sys.argv içinde string olarak gelir.
