### Part 1 Variable assignment

# Create a variable savings
savings = 100

# Print out savings
print(savings)

### Part 2 Calculations with variables

# Create a variable savings
savings = 100

# Create a variable growth_multiplier
growth_multiplier = 1.1

# Calculate result
result = savings * growth_multiplier ** 7

# Print out result
print(result)

### Part 3 Other variable types

# Create a variable desc
desc = "compound interest"

# Create a variable profitable
profitable = True

### Part 4 Guess the type

# type() command can be used to determine the data type of a variable

### Part 5

savings = 100
growth_multiplier = 1.1
desc = "compound interest"

# Assign product of savings and growth_multiplier to year1
year1 = savings * growth_multiplier

# Print the type of year1
print(type(year1))

# Assign sum of desc and desc to doubledesc
doubledesc = desc + desc

# Print out doubledesc
print(doubledesc)

### Part 6 Typer conversions

# Definition of savings and result
savings = 100
result = 100 * 1.10 ** 7

# Fix the printout
print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float
pi_float = float(pi_string)
