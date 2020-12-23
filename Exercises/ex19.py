def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Get a blanket.\n")

# pass 20 and 30 to our function - the function prints both out in three statements.
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# define cheese and cracker count for the coming function call
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
# call the function, passing it the previously defined variables to print as before.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# in this case, the two arguments are two pieces of arithmetic
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# take the defined variables above, perform arithmatic, pass into function
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
