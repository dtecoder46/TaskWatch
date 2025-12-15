import time

# Purpose: to run a stopwatch for the user's task
# Parameters: task
# Return: seconds_used
def stopwatch():
    print("\nYour time starts now!") # message to the user

    stop_status = input("Do you want to stop the stopwatch? [yes/no]: ") # stop status prompt

    seconds_used = 0 # initialize  

    while stop_status != "yes": # stopwatch continues until the user wants to stop
        time.sleep(1) # delay for 1 second acts as 1 second passing in the stopwatch

        seconds_used += 1 # tracks how long it took for the user to do a task
        
        if seconds_used % 600 == 0: 
            '''
            to ensure the user does not have to constantly input 
            while they're doing tasks and to ensure the user 
            does not abuse the prompt to end early and procrastinate 
            '''
            
            stop_status = input("Do you want to stop the stopwatch? [yes/no]: ") # stop status prompt

    print("Stopwatch has been stopped")

    return seconds_used

# Purpose: call other functions, get task input
# Parameters: none
# Return: none
def main():
    task_name = input("What task do you want to do?: ") # task input

    seconds = stopwatch()

    print(seconds)

main()