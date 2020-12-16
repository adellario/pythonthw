# Define some variables to contain escape characters and stuff - make lists
scary_goblins = "-Tall\n\t-Ginger\n\t-Bearded\n\t-Professional"
ginger_runner = "-Pale\n\t-Also Ginger\n\t-Chubby\n\t-Amateur"
killian = "-Skinny\n\t-Spanish\n\t-Extreme\n\t-Salomon Athlete"

# Define some different variables with escape characters
am_tony = "A \"runner,\" if you know what I mean."
am_mac = "Poopist\\Runner"

# Print them out using format strings
print("Ultrarunners come in all shapes and sizes:")
print(f"For instance, Gary Robbins is:\n\t{scary_goblins}")
print("")
print(f"Whereas, The Ginger Runner is:\n\t{ginger_runner}")
print("")
print(f"Whereas, The Ginger Runner is:\n\t{killian}")

print("Some other guys:")
print(f"\tTony: {am_tony}")
print(f"\tMac: {am_mac}")