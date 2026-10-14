def input_temperature(temp_str: str) -> int:
    val = int(temp_str)
    if val > 40:
        raise ValueError(f"{val}°C is too hot for plants (max 40°C)")
    elif val < 0:
        raise ValueError(f"{val}°C is too cold for plants (min 0°C)")
    return val

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
 # not: raise, hatayı Python'un kendisinin üretmesini beklemek yerine bilinçli olarak oluşturur.
