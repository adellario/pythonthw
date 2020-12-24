import math

def pythagoras(x, y):
    return math.sqrt(x ** 2 + (y ** 2))

prompt = "> "

# get a
print("Please enter the value for 'a':")
a = float(input(prompt))

# get b
print("Please enter the value for 'b':")
b = float(input(prompt))

# pass the variables to the function
c = pythagoras(a, b)

print(f"The hypotenuse is: {c}")