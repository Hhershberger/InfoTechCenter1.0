import sys
import time

print("\nWelcome to InfoTechCenter V1.0\m")


x = 0
ellipsis = 0

while x!=20:
    x+=1
    message = ("Infotech Center System Booting"+"."*ellipsis)
    ellipsis+=1
    sys.stdout.write("\r"+message)
    time.sleep(.5)
    if ellipsis==4:
        ellipsis = 0
    if x==20:
        print ("\n\nOperating System Booted up - Retina Scanned - Access Granted")