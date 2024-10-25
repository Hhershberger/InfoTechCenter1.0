
# Importing the necessary libraries
import sys  # sys module provides access to system-specific parameters and functions
import time  # time module provides time-related functions (e.g., sleep)
import random  # To randomly select weather conditions
from time import sleep  # To simulate delay in output

# ANSI escape code for blue text
BLUE = '\033[94m'  # Bright blue
RESET = '\033[0m'  # Reset to default color

# Printing a welcome message to the console in blue
print(BLUE + "\nWelcome to InfoTechCenter V1.0." + RESET)  # Use ANSI code for blue text

TimeToSleep= 2 # variable to set teh time Library to 2 seconds
time.sleep(TimeToSleep) # sets to TimeToSleep

# Initializing variables
x = 0  # x is used as a counter to control the loop iterations
ellipsis = 0  # ellipsis controls the number of dots to display in the boot message

# A while loop that simulates the booting system
while x != 20:  # Loop will run until x equals 20 (20 iterations)
    x += 1  # Increment the counter with each iteration
    message = (BLUE + "Infotech Center System Booting" + "." * ellipsis + RESET)  # Create the boot message with increasing dots
    ellipsis += 1  # Increase the number of dots for each iteration
    sys.stdout.write("\r" + message)  # Overwrite the line in the console with the new message
    time.sleep(0.5)  # Pause the loop for 0.5 seconds to create a loading effect

    # Reset ellipsis after 3 dots to avoid continuous dots beyond 3
    if ellipsis == 4:
        ellipsis = 0  # Reset ellipsis to 0 once it reaches 4 (so it cycles through 0 to 3 dots)

    # When the counter reaches 20, the system boot message is complete
    if x == 20:
        print("\n\n" + BLUE + "Operating System Booted up - Retina Scanned - Access Granted." + RESET)  # Final message after boot completes

# Print section header for weather forecast branch
print("\n**********************************************************************")
print("Weather Branch.\n")



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
        print(f"\nVRS system has been engaged only allowing you to drive {speed_limit}mph.")
    else:
        # Handle default case for normal/sunny weather
        print(f"\nThe NWS is calling for {WeatherAlert} skies. Drive carefully to get to your destination.")
        sleep(1)  # Simulate delay
        print("\nVRS system has been disengaged.")

# Call the VRS function
VRS()

# Print a decorative separator and section title
print("\n**************************************************\n")
print("Gasoline Branch.\n")

# Import necessary modules
import random
from time import sleep


# Function to randomly select a gas level from a predefined list
def gasLevelGauge():
    return random.choice(["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full"])


# Function to randomly select a gas station from a predefined list
def gasStations():
    return random.choice(["Vp", "Shell", "Meijer", "Sam's Club", "Marathon", "Mobile", "Speedway", "Circle K"])


# Function to provide alerts based on the current gas level
def gasLevelAlert():
    gasLevel = gasLevelGauge()  # Get the current gas level

    # Predefine random distances to a gas station
    milesLow = round(random.uniform(1, 25), 1)
    milesQuarterTank = round(random.uniform(25.1, 50), 1)

    # Conditions based on gas level to provide feedback
    if gasLevel == "Empty":
        print("***WARNING - YOU ARE ON EMPTY***\n")
        sleep(2)
        print("Calling Triple AAA")
    elif gasLevel == "Low":
        print("Your gas tank is Low: Check GPS for closest gas station.")
        sleep(2)
        print(f"The closest gas station is {gasStations()} in {milesLow} miles.")
    elif gasLevel == "Quarter Tank":
        print("Your gas tank is Quarter Tank: Check GPS for closest gas station.")
        sleep(2)
        print(f"The closest gas station is {gasStations()} in {milesQuarterTank} miles.")
    else:
        # For Half, Three Quarter, or Full, the user is reassured to enjoy their ride
        print(f"Your gas tank is {gasLevel}: Please enjoy your ride.")
print(gasLevelAlert())

# Execute the function to display the gas level alert

