### Part 1 Familiar functions

# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)

### Part 2 Help function

# you can call help for Python built-in functions by either
# help(function)
# or in the ipython shell:
# ?function

### Part 3 multiple arguments

# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse=True)

# Print out full_sorted
print(full_sorted)

### Python methods
# Python distinguishes between functions which take input in brackets
# function(inputs)
# and methods who are being applied to certain objects (strings, floats, lists, etc)
# object.method(inputs)

### Part 4 string methods

# string to experiment with: place
place = "poolhouse"

# Use upper() on place: place_up
place_up = place.upper()

# Print out place and place_up
print(place)
print(place_up)

# Print out the number of o's in place
print(place.count('o'))

### Part 5 list methods

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20))

# Print out how often 9.50 appears in areas
print(areas.count(9.50))

### Part 6 list methods 2

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)

### Part #7 Packages

# not all code is available at all times for all python version
# Thus you need to first install packages for certain problems
# and then import them with:
# import package
# import package as abreviation
# if you then want a function from this package type
# package.function
# you can also directly import one function directly
# from package import function
# Then you can call the function directly

### Part 8 import packages

# Definition of radius
r = 0.43

# Import the math package
import math

# Calculate C
C = 2 * r * math.pi

# Calculate A
A = math.pi * r ** 2

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))

### Part 9 selective import

# Definition of radius
r = 192500

# Import radians function of math package
from math import radians

# Travel distance of Moon over 12 degrees. Store in dist.
dist = r * radians(12)

# Print out dist
print(dist)

### Part 10 different ways of importing
# you can also import functions from subpackages and rename them
# from package.subpackage import function as abreviation


