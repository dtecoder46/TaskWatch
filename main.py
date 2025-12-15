import time

# Purpose: to read the stopwatch stop status from killswitch.yaml
# Parameters: yaml_file
# Return: stop_value
def read_killswitch(yaml_file):
    stop_status = yaml_file.read() # read the yaml file

    status_list = stop_status.split(": ")

    stop_value = status_list[1]

    return stop_value

# Purpose: to run a stopwatch for the user's task
# Parameters: task
# Return: seconds_used
def stopwatch():
    print("\nYour time starts now!") # message to the user

    file = open("killswitch.yaml", "r") # open the killswitch file

    stop = read_killswitch(file) # call the reading function

    seconds_used = 0 # initialize  

    while stop != "yes": # stopwatch continues until the user wants to stop
        time.sleep(1) # delay for 1 second acts as 1 second passing in the stopwatch

        seconds_used += 1 # tracks how long it took for the user to do a task

        stop = read_killswitch(file) # update the stop value

    return seconds_used

# Purpose: call other functions, get task input
# Parameters: none
# Return: none
def main():
    task_name = input("What task do you want to do?: ") # task input

    seconds = stopwatch()

main()