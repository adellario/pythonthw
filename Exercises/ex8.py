# Set formatter to four empty variables inside a string
formatter = "{} {} {} {}"

# Print formatter, supplanting 1, 2, 3, and 4 for the empty variables above, in that order
print(formatter.format(1, 2, 3, 4))
# Print formatter, supplanting four text strings for the four empty variables
print(formatter.format("one", "two", "three", "four"))
# Print formatter, supplanting four boolean states for the empty variables
print(formatter.format(True, False, False, True))
# Print formatter, supplanting the contents of 'formatter' for each of the empty strings - totally meta. In this case, it treats the {} as text strings
print(formatter.format(formatter, formatter, formatter, formatter))
# Print formatter, supplanting the four strings for the empty variables. But this time, use line breaks to make it tidier.
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))