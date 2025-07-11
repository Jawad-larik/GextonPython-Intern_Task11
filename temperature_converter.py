# Temperature Converter Program
# Author: Jawad Larik

# Conversion functions
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    return celsius_to_kelvin(fahrenheit_to_celsius(f))

def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))

# Temperature conversion based on units
def convert_temperature(value, from_unit, to_unit):
    from_unit = from_unit.upper()
    to_unit = to_unit.upper()

    if from_unit == to_unit:
        return value

    if from_unit == "C":
        if to_unit == "F":
            return celsius_to_fahrenheit(value)
        elif to_unit == "K":
            return celsius_to_kelvin(value)
    elif from_unit == "F":
        if to_unit == "C":
            return fahrenheit_to_celsius(value)
        elif to_unit == "K":
            return fahrenheit_to_kelvin(value)
    elif from_unit == "K":
        if to_unit == "C":
            return kelvin_to_celsius(value)
        elif to_unit == "F":
            return kelvin_to_fahrenheit(value)

    raise ValueError("Invalid conversion request")

# Main program
def main():
    print("Temperature Converter")
    print("---------------------")

    try:
        value = float(input("Enter the temperature value: "))
        from_unit = input("Convert from (C, F, K): ").strip().upper()
        to_unit = input("Convert to (C, F, K): ").strip().upper()

        if from_unit not in ['C', 'F', 'K'] or to_unit not in ['C', 'F', 'K']:
            print("Error: Please enter valid units (C, F, or K).")
            return

        result = convert_temperature(value, from_unit, to_unit)
        print(f"Result: {value}°{from_unit} is {result:.2f}°{to_unit}")

    except ValueError:
        print("Error: Invalid input. Please enter a numeric temperature and valid units.")

if __name__ == "__main__":
    main()
