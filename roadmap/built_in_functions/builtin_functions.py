# BUILT-IN FUNCTIONS

# bin(x)
# Convert an integer number to a binary string prefixed with '0b'.

print(bin(3)) # 0b11
print(bin(-10)) # -0b1010

# If the prefix "0b" is desired or not, you can use either of the following ways
print(format(14, '#b'), format(14, 'b')) # 0b1110 1110
print(f'{14:#b}', f'{14:b}')             # 0b1110 1110

# enumerate(iterable, start=0)
'''
Return an enumerate object. iterable must be a sequence, an iterator, or some other object which supports iteration. The __next__() method of the iterator returned by enumerate() returns a tuple containing a count (from start which defaults to 0) and the values obtained from iterating over iterable.
'''

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(seasons) # ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons))) # [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
print(list(enumerate(seasons, start=1))) # [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

# Loop enumerate to print index and value
lista = enumerate(seasons, start=1)
for index, value in lista:
    print(index, value)

