def input_temperature(temp_str) -> int:
    temp: int = int(temp_str)

    return temp


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")

    values = ["12", "abc"]
    for value in values:
        try:
            input_temperature(value)
            print(f"Input data is '{value}'")
            print(f"Temperature is now {value}°C")

        except Exception as e:
            print(f"Input data is '{value}'")
            print(f"Caught input_temperature error: {e}")
        print()

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
