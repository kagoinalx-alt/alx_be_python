FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def main():
    temp_input = input("Enter the temperature to convert: ")

    try:
        temperature = float(temp_input)
    except ValueError:
        raise ValueError(
            "Invalid temperature input. Please enter a numeric value.")

    unit = input(
        "Is this temperature in (C)elsius or (F)ahrenheit?(C/F) ").strip().upper()

    if unit == "C":
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature} is {converted_temp:.2f} F")
    elif unit == "F":
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature} is {converted_temp:.2f} C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")


if __name__ == "__main__":
    main()
