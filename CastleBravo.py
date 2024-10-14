print("\n**********************************************************************")

print("Weather Branch\n")

# Import Libraries
import random
from time import sleep

def weather():
    WeatherForecast=["snowing", "blizzard", "rainy", "windy", "sunny"]
    WeatherCondition=random.choice(WeatherForecast)
    return WeatherCondition

print(weather())