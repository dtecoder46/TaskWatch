import time

# Purpose: to read the logfile and get the previous record
# Parameters: none
# Return: previous_record
def readlog():
    record_list = [] # initialize a list to hold the logfile contents

    file = open("log.txt", "r") # open the logfile

    for line in file:
        record_list.append(line) # append each list to the record_list to create a list of lists

    if len(record_list) == 1: # to prevent indexing from going negative
        previous_record = []

    else:
        previous_record = record_list[len(record_list)-1] # previous record found by length - 1

    file.close()

    return previous_record

# Writes a record to the logfile containing the task name, the time used for the task, and the time difference (or delta) from the previous task
def writelog(task, time_used, last_rec):
    logfile = open("log.txt", "a") # open the logfile

    if last_rec == []: # if logfile was previously blank
        last_time = 0
        delta = ""

    else: 
        last_time = last_rec[1] # get the previous task time at index 1
        delta = time_used - last_time 

    '''
    if delta is negative, you were faster in completing a task
    if delta is positive, you were slower in completing a task
    '''

    if delta == "":
        logfile.write(task + " " + str(time_used) + "\n") # delta not recorded

    else: 
        logfile.write(task + " " + str(time_used) + " " + str(delta) + "\n") # delta recorded

    logfile.close()

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
        
        if seconds_used % 10 == 0: 
            '''
            to ensure the user does not have to constantly input 
            while they're doing tasks
            '''
            
            stop_status = input("Do you want to stop the stopwatch? [yes/no]: ") # stop status prompt

    print("Stopwatch has been stopped")

    return seconds_used

# Purpose: call other functions, get task input
# Parameters: none
# Return: none
def main():
    task_name = input("What task do you want to do?: ") # task input

    task_name.replace(" ", "_") # to ensure the task name does not get split into multiple parts

    seconds = stopwatch()

    last_record = readlog() # get the previous record

    writelog(task_name, seconds, last_record)

main()