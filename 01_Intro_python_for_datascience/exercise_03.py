### Part 1 Create a list

# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall, kit, liv, bed, bath]

# Print areas
print(areas)

### Part 2 Create lists with different types

# Adapt list areas
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]

# Print areas
print(areas)

### Part 3

# python lists can contain any type of python types
# Since python types are lists as well, lists can contain lists

### Part 4 list of lists

# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)

# Print out the type of house
type(house)

### Part 5 Subsets

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[-5])

### Part 6 subset and calculate

# Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area = areas[3] + areas[7]

# Print the variable eat_sleep_area
print(eat_sleep_area)

### Part 7 Slicing and dicing

# Use slicing to create downstairs
downstairs = areas[0:6]

# Use slicing to create upstairs
upstairs = areas[6:10]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)

### Part 8 Slicing and dicing 2

# Alternative slicing to create downstairs
downstairs = areas[:6]

# Alternative slicing to create upstairs
upstairs = areas[6:]

### Part 9 SLicing lists of lists

# list = [ [a, b] , [c, d]]
# list[1][0] = c
# first number in brackest defines the index in main list
# second number in brackets defines index in the sublist
# slicing works the same way

### Part 10 Replacing list elements

# Correct the bathroom area
areas[-1] = 10.50

# Change "living room" to "chill zone"
areas[4] = "chill zone"

### Part 11 Extend lists

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]

### part 12 Delete list elements

# You can write two different commands on the same line by adding them together separated by ;
# del(list[1]); del(lsit[-1]) will remove the second and last element of list
# be aware the all entries were assigned new indices after the first command

### part 13 inner workings of lists

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy
areas_copy = areas
# this assign the variable areas_copy to the same memory location as areas
# thus, if you change the list areas_copy, you also change areas!
# to assign areas_copy a new memory location with the same entries as areas do this
areas_copy = areas[:]
# or
areas_copy = list(areas)

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
