from sys import argv

script, input_file = argv

# this function reads the opened file and prints its contents entirely
# I think 'f' will do this for any open file.
def print_all(f):
    print(f.read())

# This function rewinds to 'byte 0' in the file
def rewind(f):
    f.seek(0)

# this takes a variable, line count, prints it, and then the corresponding line
def print_a_line(line_count, f):
    print(line_count, f.readline())

# open the file and assign it to current_file
current_file = open(input_file)

print("First, let's print the whole file:\n")

# pass current_file into the print_all function to print it
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# pass current_file in to the rewind function to rewind it
rewind(current_file)

print("Let's print three lines:")

# set the line number to 1, then use the print_a_line function to print line 1
current_line = 1
print_a_line(current_line, current_file)

# iterate the line number to print line 2
current_line = current_line + 1
print_a_line(current_line, current_file)

# iterate once more to print line 3
current_line = current_line + 1
print_a_line(current_line, current_file)