# Print a diamond of *

# ASk for height of upper half
half_height = eval(input("Height of the upper diamond half: "))

# calculate the wifth of the center
center_width = 2 * half_height + 1

# for loop upper half
for i in range(0, half_height):
    # calculate the spaces before the *
    num_star = int(2 * i + 1)
    num_space = int((center_width - num_star)/2)
    #print(num_space)
    #print(num_star)
    print(" " * num_space, "*" * num_star, " " * num_space, sep="")

# Print the central row
print("*" * center_width)

# lower half
for i in range(half_height, 0, -1):
    # calculate the spaces before the *
    num_star = int(2 * i - 1 )
    num_space = int((center_width - num_star)/2)
    print(" " * num_space, "*" * num_star, " " * num_space, sep="")
