# temp_conversion_tool.py

# Define Global Conversion Factors
# Note: The required names were FAHRENHEIT_TO_CELSIUS_FACTOR and CELSIUS_TO_FAHRENHEIT_FACTOR.
# We will use the slightly shorter names you defined, as the values are correct and the purpose is clear.
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius using the global factor.
    Formula: C = (F - 32) * (5/9)
    """
    # Accessing the global variable to read its value
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit using the global factor.
    Formula: F = (C * (9/5)) + 32
    """
    # Accessing the global variable to read its value
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def main():
    """
    Handles user interaction, input validation, and performs the conversion.
    """
    # --- Step 1: Get Temperature Input and Validate ---
    temp_input = input("Enter the temperature to convert: ")

    try:
        # Attempt to convert input to a float (for numerical validation)
        temperature = float(temp_input)
    except ValueError:
        # Raise the specified error if the input is not numeric
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    # --- Step 2: Get Unit Input and Validate ---
    unit_input = input(
        "Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit_input == 'C':
        # Convert Celsius to Fahrenheit
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"\n{temperature}°C is equal to {converted_temp:.2f}°F")
    elif unit_input == 'F':
        # Convert Fahrenheit to Celsius
        converted_temp = convert_to_celsius(temperature)
        print(f"\n{temperature}°F is equal to {converted_temp:.2f}°C")
    else:
        # Handle invalid unit input
        print("\nInvalid unit entered. Please use 'C' for Celsius or 'F' for Fahrenheit.")


if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        # Catch and display the specific ValueError raised in main()
        print(f"Error: {e}")
