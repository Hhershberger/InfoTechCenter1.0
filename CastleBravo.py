# Print section header for weather forecast branch
print("\n**********************************************************************")
print("Weather Branch\n")

# Importing necessary libraries
import random  # To randomly select weather conditions
from time import sleep  # To simulate delay in output


# Function to get a random weather condition
def Weather():
    # List of possible weather conditions
    WeatherForecast = ["snowy", "blizzard", "rainy", "windy", "icy", "sunny"]
    # Randomly select a weather condition from the list
    WeatherCondition = random.choice(WeatherForecast)
    return WeatherCondition


# Call the Weather function and store the returned condition in WeatherAlert
WeatherAlert = Weather()


# Function to simulate Vehicle Restriction System (VRS) behavior based on weather
def VRS():
    # If the weather is snowy, update alarm and set speed limit
    if WeatherAlert == "snowy":
        print("\nThe National Weather Service has updated our alarm by 30 minutes because"
              " of the forecast of", WeatherAlert, "weather conditions.")
        sleep(1)  # Simulate delay
        print("\nVRS system has been engaged only allowing you to drive 55mph")

    # If the weather is blizzard, update alarm and set speed limit
    elif WeatherAlert == "blizzard":
        print("\nThe National Weather Service has updated our alarm by 45 minutes because"
              " of the forecast of", WeatherAlert, "weather conditions.")
        sleep(1)  # Simulate delay
        print("\nVRS system has been engaged only allowing you to drive 45mph")

    # If the weather is rainy, update alarm and set speed limit
    elif WeatherAlert == "rainy":
        print("\nThe National Weather Service has updated our alarm by 15 minutes because"
              " of the forecast of", WeatherAlert, "weather conditions.")
        sleep(1)  # Simulate delay
        print("\nVRS system has been engaged only allowing you to drive 65mph")

    # If the weather is windy, update alarm and set speed limit
    elif WeatherAlert == "windy":
        print("\nThe National Weather Service has updated our alarm by 5 minutes because"
              " of the forecast of", WeatherAlert, "weather conditions.")
        sleep(1)  # Simulate delay
        print("\nVRS system has been engaged only allowing you to drive 70mph")

    # If the weather is icy, update alarm and set speed limit
    elif WeatherAlert == "icy":
        print("\nThe National Weather Service has updated our alarm by 50 minutes because"
              " of the forecast of", WeatherAlert, "weather conditions.")
        sleep(1)  # Simulate delay
        print("\nVRS system has been engaged only allowing you to drive 30mph")

    # If no special weather condition, print default message
    else:
        print("\nThe NWS is calling for", WeatherAlert, "skies. Drive carefully to get to your destination")
        sleep(1)  # Simulate delay
        print("\nVRS system has been disengaged")


# Call the VRS function and print the result
print(VRS())
