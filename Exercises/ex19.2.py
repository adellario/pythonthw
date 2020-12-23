# define the custom function;
# the function displays the two inputs, then adds them and prints that.
def activity_count(bike_count, run_count):
    print(f"You went on {bike_count} rides this year.")
    print(f"You went on {run_count} runs this year.")
    total_activities = bike_count + run_count
    print(f"In total, you had {total_activities} activities this year.\n")

# set a prompt for user input
prompt = "> "

# accept integer as total ride count
print("Please enter the number of bike rides you took this year:")
rides = int(input(prompt))

# accept integer as total run count
print("Please enter the number of runs you went on this year:")
runs = int(input(prompt))

# pass values to function
activity_count(rides, runs)

# create a divider between function call types
print('*' * 15)

#
# Section 2 - for later: figure out how to make this more efficient
#

# now obtain a file to get the rides, maybe?
print("Give me a file with your total rides in it:")
ride_file = input("> ")

# read the file and convert to integer
ride_read = open(ride_file)
rides_from_file = ride_read.read()
rides_int = int(rides_from_file)

# obtain a file to read the runs
print("Give me a file with your total runs in it:")
run_file = input("> ")

# read the file and convert to integer
run_read = open(run_file)
runs_from_file = run_read.read()
runs_int = int(runs_from_file)

# now call the function
activity_count(rides_int, runs_int)

# close 'em
ride_read.close()
run_read.close()