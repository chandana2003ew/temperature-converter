def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

print("Temperature Converter")
print("Available scales: Celsius (C), Fahrenheit (F), Kelvin (K)")

source = input("Enter source scale (C/F/K): ").upper()
value = float(input("Enter temperature value: "))
target = input("Enter target scale (C/F/K): ").upper()

if source == target:
    print(f"No conversion needed. Result: {value}°{target}")

elif source == "C":
    if target == "F":
        print(f"{value}°C = {celsius_to_fahrenheit(value):.2f}°F")
    elif target == "K":
        print(f"{value}°C = {celsius_to_kelvin(value):.2f}K")

elif source == "F":
    if target == "C":
        print(f"{value}°F = {fahrenheit_to_celsius(value):.2f}°C")
    elif target == "K":
        print(f"{value}°F = {fahrenheit_to_kelvin(value):.2f}K")

elif source == "K":
    if target == "C":
        print(f"{value}K = {kelvin_to_celsius(value):.2f}°C")
    elif target == "F":
        print(f"{value}K = {kelvin_to_fahrenheit(value):.2f}°F")

else:
    print("Invalid input. Please enter C, F, or K.")
