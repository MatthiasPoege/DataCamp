# Print a triangle of *

# Ask how high it should be
height = eval(input("Height of the triangle: "))

for i in range(height):
    print("*" * (i + 1))
