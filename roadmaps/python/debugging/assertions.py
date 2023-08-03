'''
Assertions
An assertion is a sanity check to make sure your code isn’t doing something obviously wrong. These sanity checks are performed by assert statements. If the sanity check fails, then an AssertionError exception is raised. In code, an assert statement consists of the following:

The assert keyword
A condition (that is, an expression that evaluates to True or False)
A comma
A string to display when the condition is False
In plain English, an assert statement says, “I assert that the condition holds true, and if not, there is a bug somewhere, so immediately stop the program.”
'''

ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.sort() # [15, 17, 22, 26, 47, 54, 57, 73, 80, 92]

print(ages)
assert ages[0] <= ages[-1] # No output, expression evaluates to True, the assert statement does nothing.

# But if we change the line 13 for this
ages.reverse()
print(ages) # [92, 80, 73, 57, 54, 47, 26, 22, 17, 15]
assert ages[0] <= ages[-1] # Expression evaluates to False, program throws an AssertionError

# So, the program will not continue since previous AssertionError
print("I will not be executed...")