# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.
    """
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    """
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    try:
        # Prompt user for temperature and unit
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

        if unit == 'F':
            converted_temperature = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temperature:.2f}°C")
        elif unit == 'C':
            converted_temperature = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temperature:.2f}°F")
        else:
            print("Invalid temperature unit. Please enter 'C' or 'F'.")

    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
