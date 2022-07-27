### Part1 list comprehensions
# list comprehensions are single lines of code to simplify for loops over lists
# new_list = [output_expression for iterator_variable in iterable]
# they can also be nested functions - meaning two or more for loops pe line

### Part2 basic list comprehension
doctor = ['house', 'cuddy', 'chase', 'thirteen', 'wilson']
firt_char = [doc[0] for doc in doctor]

### Part3 writing list comprehensions
# Create list comprehension: squares
squares = [i ** 2 for i in range(10)]

### Part4 nested list comprehensions
# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(5)] for row in range(5)]

# Print the matrix
for row in matrix:
    print(row)