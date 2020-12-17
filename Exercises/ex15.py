# Importing the argument variable to enable arguments at runtime
from sys import argv

# Defininig the arguments to be taken and setting them to variables
script, filename = argv

# Begin with a prompt for the filename
# filename = input("Please enter the filename: ")

# Setting txt to the contents of an opened filename specified by way of argument
txt = open(filename)

# Print the name of the file, and then tell the program to read it out
print(f"Here's your file {filename}:")
print(txt.read())

# Close the first file
txt.close()

# Print a prompt for the filename again and set the contents to a variable as above
print("Type the filename again:")
file_again = input("> ")

# Read the file and set its contents to a variable as a string
txt_again = open(file_again)

# Print out the contents of the file string
print(txt_again.read())

# Close the second file
txt_again.close()