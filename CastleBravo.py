# Print a decorative separator and section title
print("\n**************************************************\n")
print("Gasoline Branch\n")

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
        print("Your gas tank is Low: Check GPS for closest gas station")
        sleep(2)
        print(f"The closest gas station is {gasStations()} in {milesLow} miles")
    elif gasLevel == "Quarter Tank":
        print("Your gas tank is Quarter Tank: Check GPS for closest gas station")
        sleep(2)
        print(f"The closest gas station is {gasStations()} in {milesQuarterTank} miles")
    else:
        # For Half, Three Quarter, or Full, the user is reassured to enjoy their ride
        print(f"Your gas tank is {gasLevel}: Please enjoy your ride")


# Execute the function to display the gas level alert
gasLevelAlert()
