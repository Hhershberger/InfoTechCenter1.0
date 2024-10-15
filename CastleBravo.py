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
        sleep(1)
        print("\nVRS system has been engaged only allowing you to drive 55mph")
    elif WeatherAlert=="blizzard":
        print("\nThe National Weather Service has updated our alarm by 45 minutes because"
              " of the forecast of", WeatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS system has been engaged only allowing you to drive 45mph")

print(VRS())