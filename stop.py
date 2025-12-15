file = open("killswitch.yaml", "w") # open the yaml file

stop_status = input("Do you want to stop the stopwatch? [yes/no]: ") # stop status prompt

while stop_status != "yes": # user doesn't want the stopwatch to stop
    file.write(stop_status) # Write status to file

    stop_status = input("Do you want to stop the stopwatch? [yes/no]: ") # re-prompt since the user hasn't said "yes" yet

file.write(stop_status) # Write to file if the user said "yes" on the first prompt