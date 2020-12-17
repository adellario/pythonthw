from sys import argv
script, firstname, lastname = argv

print(f"Hello, {firstname} {lastname}!")
print("Welcome to MaxTrainingRunCalc v.2!")
print("*" * 15)

race_length = int(input("Please enter your race length: "))

max_train_distance = race_length / 2
print(f"Your maximum training run should be {max_train_distance} miles long.")