name = 'Tony Dell\'Ario'
age = 36 # One year older than Zed
weight = 175 # lbs - who knows if that's true
height_in = 74 # inches
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

# Convert height to cm
height_cm = height_in * 2.54

# Convert weight to kg
weight_kg = weight * 0.453592

print(f"Let's talk about {name}.")
print(f"He's {height_in} inches tall.")
print(f"Or if you're a snooty European, his height is {height_cm} centimeters.")
print(f"He's {weight} pounts heavy")
print(f"Again, for the snoots: He weighs {weight_kg}kgs.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height_in + weight
print(f"If I add {age}, {height_in}, and {weight} I get {total}.")