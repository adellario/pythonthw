# Illustrate the tab, new line, and backslash escape characters by using them in vars set to strings including them.
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

# Set a new var to a three-quote-long sting, also showing the new line and tab escape characters
# Check out line 13 - it new lines and then tabs in to make that last item appear like the others despite being on the same line.
# Also, you can't put a comment inside a """
fat_cat = """
I'll do a list:
\t* Cat food
\t* Finishes
\t* Catnip\n\t* Grass 
"""

# Print 'em.
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)