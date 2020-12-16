# Establish the joke by setting the variable for types of people
types_of_people = 10
# Set x to a string that contains the variable set above instead of keeping it static
x = f"There are {types_of_people} types of people."

# Set 'binary' and 'do_not', insert them as variables into a string, and set that string to y
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# Print the first string, line break, print the second string (set above)
print(x)
print(y)

# Print a string including x set above; then do the same with y
print(f"I said: {x}")
print(f"I also said: {y}")

# Set hilarious to False and set joke_evaluation to a string followed by empty brackets
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# Print the joke_evaluation string, applying the False text as a format flag
print(joke_evaluation.format(hilarious))

# Set two variables to contain strings
w = "This is the left side of..."
e = "a string with a right side."

# Then print them by contatenation
print(w + e)