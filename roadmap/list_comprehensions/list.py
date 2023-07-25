# Without list comprehension you will have to write a for
# statement with a conditional test inside.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = []

for x in fruits:
    if "a" in x:
        new_list.append(x)
  
print(new_list) # ['apple', 'banana', 'mango']

# With list comprehension you can do all that with only one line of code:

new_list = [x for x in fruits if "a" in x]
print(new_list) # ['apple', 'banana', 'mango']

# If the expression is a tuple (e.g. the (x, y) in the previous example), it must be parenthesized.

vec = [-4, -2, 0, 2, 4]
# Create a new list with the values doubled
print([x * 2 for x in vec]) # [-8, -4, 0, 4, 8]

# Filter the list to exclude negative numbers
print([x for x in vec if x >= 0]) # [0, 2, 4]

# Apply a function to all the elements
print([abs(x) for x in vec]) # [4, 2, 0, 2, 4]

# Call a method on each element
freshfruit = ['   banana   ', '   loganberry   ', 'passion fruit   ']
print([weapon.strip() for weapon in freshfruit]) # ['banana', 'loganberry', 'passion fruit']

# create a list of 2-tuples like (number, square)
# The tuple must be parenthesized, otherwise an error is raised
print([(x, x**2) for x in range(6)]) # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# Flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem]) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# List Comprehensions can contain complex expressions and nested functions
from math import pi
print([str(round(pi, i)) for i in range(1, 6)]) # ['3.1', '3.14', '3.142', '3.1416', '3.14159']

# Nested List Comprehensions
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print([[row[i] for row in matrix] for i in range(4)]) # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# In real world, you should prefer built-in functions to complex flow
# statements. The zip() function would do a great job for this use case:
print(list(zip(*matrix))) # [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]