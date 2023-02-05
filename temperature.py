temperature = None
tempType = None

def wind_chill(temp, wind_speed):
    return 35.74 + 0.6215 * temp - 35.75 * (wind_speed**0.16) + 0.4275 * temp * (wind_speed**0.16)

def convertToFahrenheit(temp_c): 
    return round((temp_c * 9.0 / 5.0) + 32.0, 2)

while True:
    try:
        temperature = float(input("What is the temperature? "))
    except ValueError:
        print("Please, enter a valid temperature.")
        continue
    else:
        break

while True:
    try:
        tempType = str(input("Fahrenheit or Celsius (F/C)? ").upper())
    except ValueError:
        print("Please, enter a valid temperature type.")
        continue
    else:
        if tempType == 'C' or tempType == 'F':
            break
        else:
            print("Please, enter a valid temperature type.")

if(tempType == 'C'):
    temperature = convertToFahrenheit(temperature)

for wind in range(5,65,5):
   print(f'At temperature {temperature}F, and wind speed {wind} mph, the windchill is: {wind_chill(temperature, wind):.2f}F')
