print("\n**************************************************\n")

print("Gasoline Branch")

import random
from time import sleep

def gasLevelGauge():
    gasLevelList=["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full"]
    return random.choice(gasLevelList)

def gasStations():
    gasStationsList=["Vp","Shell","Meijer","Sam's Club","Marathon","Mobile","Speedway","Circle K"]
    return random.choice(gasStationsList)

#def gasLevelAlert():
