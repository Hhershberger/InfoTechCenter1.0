print("\n**********************************************************************")

print("Weather Branch\n")

# Import Libraries
import random
from time import sleep

def Weather():
    WeatherForecast=["snowy", "blizzard", "rainy", "windy", "sunny"]
    WeatherCondition=random.choice(WeatherForecast)
    return WeatherCondition

WeatherAlert= Weather()

def VRS():
    if WeatherAlert==("snowy"):
        print("\nThe National Weather Service has updated our alarm by 30 minutes because"
              " of the forecast of", WeatherAlert, "weather conditions.")
print(VRS())