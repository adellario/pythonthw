import math

def square(x):
    return x ** 2

prompt = "> "

# get a
print("Please enter the value for 'a':")
a = int(input(prompt))

# get b
print("Please enter the value for 'b':")
b = int(input(prompt))

# calculate c squared
a_square = square(a)
b_square = square(b)
c_square = a_square + b_square

# find the square root of c and print
c = math.sqrt(c_square)

print(f"The hypotenuse is: {c}")