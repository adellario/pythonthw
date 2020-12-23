from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# We could do these on one line; how? (see ex17.2.py)
# Open what we defined as the from_file and set it to in_file
# read in_file and set it as indata
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long.")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

# open what we defined as to_file, making it writable, and define that as out_file
# write the contents of indata as out_file
out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()