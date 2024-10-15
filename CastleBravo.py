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
    elif WeatherAlert=="rainy":
        print("\nThe National Weather Service has updated our alarm by 15 minutes because"
              " of the forecast of", WeatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS system has been engaged only allowing you to drive 65mph")
    elif WeatherAlert=="windy":
        print("\nThe National Weather Service has updated our alarm by 5 minutes because"
              " of the forecast of", WeatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS system has been engaged only allowing you to drive 70mph")
    elif WeatherAlert=="icy":
        print("\nThe National Weather Service has updated our alarm by 50 minutes because"
              " of the forecast of", WeatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS system has been engaged only allowing you to drive 30mph")
    else:
        print("\nThe NWS is calling for", WeatherAlert, "skies. Drive carefully to get to your destination")
        sleep(1)
        print("\nVRS system has been disengaged")

print(VRS())