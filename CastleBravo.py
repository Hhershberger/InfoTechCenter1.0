# Importing the necessary libraries
import sys  # sys module provides access to system-specific parameters and functions
import time  # time module provides time-related functions (e.g., sleep)

# ANSI escape code for blue text
BLUE = '\033[94m'  # Bright blue
RESET = '\033[0m'  # Reset to default color

# Printing a welcome message to the console in blue
print(BLUE + "\nWelcome to InfoTechCenter V1.0" + RESET)  # Use ANSI code for blue text

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
        print("\n\n" + BLUE + "Operating System Booted up - Retina Scanned - Access Granted" + RESET)  # Final message after boot completes
