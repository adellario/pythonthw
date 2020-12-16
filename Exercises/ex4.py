# Define car count
cars = 100
# Define the volume of each car in "people"
space_in_a_car = 4.0
# Define the number of drivers
drivers = 30
# Define the number of passengers
passengers = 90
# Calculate the number of cars not driven by subtracting total drivers from total cars
cars_not_driven = cars - drivers
# Define cars being driven as many as there are drivers
cars_driven = drivers
# Set carpool capacity to the nubmer of cars driven multiplied by the defined car space
carpool_capacity = cars_driven * space_in_a_car
# Find average passengers per car by dividing carpool capacity by cars driven
average_passengers_per_car = carpool_capacity / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")