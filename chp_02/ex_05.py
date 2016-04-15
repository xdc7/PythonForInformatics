def convertFahToCel(t):
    return (t - 32) * 5 /9

def convertCelToFah(t):
    return (t  * 9 /5) + 32


while(True):
    temperatureUnit = input("Enter F or C to convert to C or F respectively or q to quit: ")

    if temperatureUnit.lower() == "f":
        temperature = float(input("Enter temperature in Fahrenheit: "))
        print(convertFahToCel(temperature))
    elif temperatureUnit.lower() == "c":
        temperature = float(input("Enter temperature in Celsius: "))
        print(convertCelToFah(temperature))
    else:
        break