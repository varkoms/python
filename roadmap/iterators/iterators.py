# Python iter() example
string = "GFG"
ch_iterator = iter(string)

print(next(ch_iterator)) # G
print(next(ch_iterator)) # F
print(next(ch_iterator)) # G

"""
Creating and looping over an iterator using iter() and next()
Below is a simple Python Iterator that creates an iterator type that iterates from 10 to a given limit. For example, if the limit is 15, then it prints 10 11 12 13 14 15. And if the limit is 5, then it prints nothing.
"""

class Test:
    # Constructor
    def __init__(self, limit):
        self.limit = limit

    # Creates iteractor object
    # Called when iteration is initialized
    def __iter__(self):
        self.x = 10
        return self
    
    # To move to the next element
    # we should replace next with __next__
    def __next__(self):
        # Store current value ofx
        x = self.x

        # Stop iteration if limit is reached
        if x > self.limit:
            raise StopIteration
        
        # Else increment and return old value
        self.x = x + 1
        return x
    
# Prints numbers from 10 to 15
for i in Test(15):
    print(i)

# Print nothing
for i in Test(5):
    print(i)

# Iterating over built-in iterable using iter() method
# In the following iterations, the iteration state and iterator variable is managed internally (we can’t see it) using an iterator object to traverse over the built-in iterable like list, tuple, dict, etc.

# Iterating over a list
print("List Iteration")
l = ["geeks", "for", "geeks"]

for i in l:
    """
    List Iteration
    geeks
    for
    geeks
    """
    print(i)

# Iterating over a tuple(immutable)
print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
    """
    Tuple Iteration
    geeks
    for
    geeks
    """
    print(i)

# Iterating over a string
print("\nString iteration")
s = "Geeks"
for i in s:
    """
    String iteration
    G
    e
    e
    k
    s
    """
    print(i)

# Iterating over dictionary
print("\nDictionary iteration")
d = dict()
d["xyz"] = 123
d["abc"] = 345
for i in d:
    """
    xyz  123
    abc  345
    """
    print("%s  %d" %(i, d[i]))