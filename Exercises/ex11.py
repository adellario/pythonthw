# Print a question and prevent appending a newline character so the program accepts the input
# There's a space between the ''s so the input prompt doesn't butt up against the question
# Do this for each question
print("How old are you?", end=' ')
age = input() # accept user input for the variable
print("how tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

# Format print the vars in a string.
print(f"So, you're {age} years old, {height} tall, and weigh {weight} pounds.")