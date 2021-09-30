name = 'Zed A. Shaw'
age = 35  # Not a lie
height = 74  # inches
weight = 180  # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Lest's talk about {name}.")
print(f"He's {height} inches tall")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"Hes teeth are ususally {teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and my {weight} I get {total}")

# convert inches to cm and lbs to kg
cmHeight = height * 2.54
kgWeight = weight * 0.453592

print(
    f"If you are metric not imperial then my height is {round(cmHeight)}cm and my weight {round(kgWeight)}kg")
