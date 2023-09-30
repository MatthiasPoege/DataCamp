# Print a rectangle of *

# Ask how wide it should be
width = eval(input("Width of the rectangle: "))

# Ask how high it should be
height = eval(input("Height of the rectangle: "))

for i in range(height):
    print("*" * width)

