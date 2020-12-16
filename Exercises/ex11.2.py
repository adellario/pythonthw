# This program calculates your longest maximum training run distance.
# First, ask some basic questions.
first_name = input("What's your first name? ")
last_name = input("What's your last name? ")
race_length = int(input("How long is your race? "))

# Calculate the max training run length
max_train_run = race_length / 2

# Print the result
print(f"Hello, {first_name} {last_name}!\nCongratulations on signing up for a {race_length} mile race!")
print(f"Your maximum training run distance should be:\n\t\t***{max_train_run} miles long.")
print("Good luck!")