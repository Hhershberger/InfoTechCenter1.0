# Print a decorative separator for output readability
print("\n**************************************************\n")

# Print the branch or section title
print("Gasoline Branch\n")

# Importing the random module for selecting random gas levels and stations
# Importing sleep from the time module to simulate pauses in the output
import random
from time import sleep


# Function to randomly select a gas level from a predefined list
def gasLevelGauge():
    # List of possible gas levels
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full"]
    # Randomly choose a gas level from the list and return it
    return random.choice(gasLevelList)


# Function to randomly select a gas station from a predefined list
def gasStations():
    # List of possible gas stations
    gasStationsList = ["Vp", "Shell", "Meijer", "Sam's Club", "Marathon", "Mobile", "Speedway", "Circle K"]
    # Randomly choose a gas station from the list and return it
    return random.choice(gasStationsList)


# Function to provide alerts based on the current gas level
def gasLevelAlert():
    # Randomly generate a distance to a gas station when gas level is Low (between 1 and 25 miles)
    milesToGasStationLow = round(random.uniform(1, 25), 1)
    # Randomly generate a distance to a gas station when gas level is at Quarter Tank (between 25.1 and 50 miles)
    milesToGasStationQuarterTank = round(random.uniform(25.1, 50), 1)

    # Get the current gas level by calling the gasLevelGauge function
    gasLevelIndicator = gasLevelGauge()

    # Check the gas level and provide appropriate feedback
    if gasLevelIndicator == "Empty":
        # If the tank is empty, warn the user and simulate a call to AAA
        print("***WARNING - YOU ARE ON EMPTY***\n")
        sleep(2)
        print("Calling Triple AAA")
    elif gasLevelIndicator == "Low":
        # If the gas is low, suggest checking GPS for the closest station and display a random station
        print("Your gas tank is on Low: Check GPS for closest gas station")
        sleep(2)
        print("The closest gas station is", gasStations(), "in", milesToGasStationLow, "miles")
    elif gasLevelIndicator == "Quarter Tank":
        # If the gas is at Quarter Tank, suggest checking GPS and show a station within a further range
        print("Your gas tank is on Quarter Tank: Check GPS for closest gas station")
        sleep(2)
        print("The closest gas station is", gasStations(), "in", milesToGasStationQuarterTank, "miles")
    elif gasLevelIndicator == "Half Tank":
        # If the tank is half full, no immediate action is needed, just enjoy the ride
        print("Your gas tank is on Half Tank: Please enjoy your ride")
    elif gasLevelIndicator == "Three Quarter Tank":
        # If the tank is three-quarters full, reassure the user they can continue enjoying their ride
        print("Your gas tank is on Three Quarter Tank: Please enjoy your ride")
    else:
        # If the tank is full, the user can enjoy their ride without worries
        print("Your gas tank is on Full: Please enjoy your ride")


# Call the gasLevelAlert function and print its result (if any)
print(gasLevelAlert())
