# Print an empty rectangle of *

# Ask how wide it should be
width = eval(input("Width of the rectangle: "))

# Ask how high it should be
height = eval(input("Height of the rectangle: "))

print("*" * width)

for i in range(height):
    print("*", "*", sep=" "*(width-2))

print("*" * width)
