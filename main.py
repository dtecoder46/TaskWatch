import time

# Purpose: to run a stopwatch for the user's task
# Parameters: task
# Return: TBD
def stopwatch():
    print("\nYour time starts now!") # message to the user

    for seconds in range(1, 11): # temporary
        time.sleep(1) # delay for 1 second acts as 1 second passing in the stopwatch

# Purpose: call other functions, get task input
# Parameters: none
# Return: none
def main():
    task_name = input("What task do you want to do?: ") # task input

