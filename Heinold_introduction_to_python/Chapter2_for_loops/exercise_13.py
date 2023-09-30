# Print an inverted triangle of *

# Ask how high it should be
height = eval(input("Height of the triangle: "))

for i in range(height, 0, -1):
    print("*" * i)
