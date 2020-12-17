from sys import argv

script, user_name, user_age = argv
prompt = "<$> "

print(f"Hi {user_name}!")
print("Welcome to MaxTrainingRunCalc v.3!")
print("*" * 30)

print("Which race are you running?")
race_name = input(prompt)

print("When is your race?")
race_date = input(prompt)

print("How is your race distance measured?")
race_units = input(prompt)

print("How long is your race?")
race_length = int(input(prompt))

max_train_distance = race_length / 2

print(f'''
Fantastic! You're going to do great, {user_name}!
Good luck in the {race_name} on {race_date}!
At your age, {user_age}, you should try to limit
your maximum training run to {max_train_distance}{race_units}.
''')