def input_temperature(temp_str: str) -> int:
    return int(temp_str)

def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print()

    try:
        print("Input data is '25'")
        temperature = input_temperature("25")
        print(f"Temperature is now {temperature}°C")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
        
    print()

    try:
        print("Input data is 'abc'")
        temperature = input_temperature("abc")
        print(f"Temperature is now {temperature}°C")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
        
    print()
    print("All tests completed - program didn't crash!")

if __name__ == "__main__":
    test_temperature()
 # not: Burada amaç, hatayı programı çökertmeden try/except ile yakalamayı öğrenmek.
