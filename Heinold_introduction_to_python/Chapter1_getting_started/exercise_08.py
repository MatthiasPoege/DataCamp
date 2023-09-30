# Calculate sum and mean of three input numbers

# Ask for three input numbers
num1 = eval(input("Enter input number #1: "))
num2 = eval(input("Enter input number #2: "))
num3 = eval(input("Enter input number #3: "))

# Calculate the sum
total = num1 + num2 + num3

# calculate the mean
avg = total/3

# print the results
print("The sum of the input numbers is: ", total, ".", sep="")
print("The average of the input numbers is: ", avg, ".", sep="")
