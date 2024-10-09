# Importing the necessary libraries
import sys  # sys module provides access to system-specific parameters and functions
import time  # time module provides time-related functions (e.g., sleep)

# Printing a welcome message to the console
print("\nWelcome to InfoTechCenter V1.0\m")  # \m seems like a typo; it should probably be \n for a new line

# Initializing variables
x = 0  # x is used as a counter to control the loop iterations
ellipsis = 0  # ellipsis controls the number of dots to display in the boot message

# A while loop that simulates the booting system
while x != 20:  # Loop will run until x equals 20 (20 iterations)
    x += 1  # Increment the counter with each iteration
    message = ("Infotech Center System Booting" + "." * ellipsis)  # Create the boot message with increasing dots
    ellipsis += 1  # Increase the number of dots for each iteration
    sys.stdout.write("\r" + message)  # Overwrite the line in the console with the new message
    time.sleep(0.5)  # Pause the loop for 0.5 seconds to create a loading effect

    # Reset ellipsis after 3 dots to avoid continuous dots beyond 3
    if ellipsis == 4:
        ellipsis = 0  # Reset ellipsis to 0 once it reaches 4 (so it cycles through 0 to 3 dots)

    # When the counter reaches 20, the system boot message is complete
    if x == 20:
        print("\n\nOperating System Booted up - Retina Scanned - Access Granted")  # Final message after boot completes
