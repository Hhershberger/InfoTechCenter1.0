print("\n**************************************************\n")

print("Gasoline Branch\n")

import random
from time import sleep

def gasLevelGauge():
    gasLevelList=["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full"]
    return random.choice(gasLevelList)

def gasStations():
    gasStationsList=["Vp","Shell","Meijer","Sam's Club","Marathon","Mobile","Speedway","Circle K"]
    return random.choice(gasStationsList)

def gasLevelAlert():
    milesToGasStationLow=round(random.uniform(1,25),1)
    milesToGasStationQuarterTank=round(random.uniform(25.1,50),1)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator=="Empty":
        print("***WARNING - YOU ARE ON EMPTY***\n")
        sleep(2)
        print("Calling Triple AAA")
    elif gasLevelIndicator=="Low":
        print("Your gas tank is on Low: Check GPS for closest gas station")
        sleep(2)
        print("The closest gas station is",gasStations(),"in",milesToGasStationLow,"miles")
    elif gasLevelIndicator=="Quarter Tank":
        print("Your gas tank is on Quarter Tank: Check GPS for closest gas station")
        sleep(2)
        print("The closest gas station is", gasStations(), "in", milesToGasStationQuarterTank, "miles")
    elif gasLevelIndicator=="Half Tank":
        print("Your gas tank is on Half Tank: Please enjoy your ride")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is on Three Quarter Tank: Please enjoy your ride")
    else:
        print("Your gas tank is on Full: Please enjoy your ride")
print(gasLevelAlert())