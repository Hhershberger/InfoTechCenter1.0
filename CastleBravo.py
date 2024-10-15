# Print section header for weather forecast branch
print("\n**********************************************************************")
print("Weather Branch\n")

# Importing necessary libraries
import random  # To randomly select weather conditions
from time import sleep  # To simulate delay in output

# Function to get a random weather condition
def Weather():
    # List of possible weather conditions
    WeatherForecast = ["snowy", "blizzard", "rainy", "windy", "sunny"]
    # Randomly select a weather condition from the list
    return random.choice(WeatherForecast)

# Call the Weather function and store the returned condition in WeatherAlert
WeatherAlert = Weather()

# Dictionary to store weather conditions, alarm updates, and speed limits
weather_conditions = {
    "snowy": (30, 55),
    "blizzard": (45, 45),
    "rainy": (15, 65),
    "windy": (5, 70),
    "icy": (50, 30)  # Note: icy is not in the forecast list, but handled just in case
}

# Function to simulate Vehicle Restriction System (VRS) behavior based on weather
def VRS():
    if WeatherAlert in weather_conditions:
        # Get alarm delay and speed limit based on weather condition
        alarm_delay, speed_limit = weather_conditions[WeatherAlert]
        print(f"\nThe National Weather Service has updated our alarm by {alarm_delay} minutes because"
              f" of the forecast of {WeatherAlert} weather conditions.")
        sleep(1)  # Simulate delay
        print(f"\nVRS system has been engaged only allowing you to drive {speed_limit}mph")
    else:
        # Handle default case for normal/sunny weather
        print(f"\nThe NWS is calling for {WeatherAlert} skies. Drive carefully to get to your destination.")
        sleep(1)  # Simulate delay
        print("\nVRS system has been disengaged")

# Call the VRS function
VRS()
