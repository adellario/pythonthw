import math

def pythagoras(x, y):
    return (x ** 2) + (y ** 2) 

prompt = "> "

# get a
print("Please enter the value for 'a':")
a = int(input(prompt))

# get b
print("Please enter the value for 'b':")
b = int(input(prompt))

# pass the variables to the function
c_squared = pythagoras(a, b)

# find the square root of c and print
c = math.sqrt(c_squared)

print(f"The hypotenuse is: {c}")