# Python function with parameters
def add(num1: int, num2: int) -> int:
    num3 = num1 + num2
    return num3

num1, num2 = 5, 15
ans = add(num1, num2)
print(f'The addition of {num1} and {num2} results {ans}')

# Default Arguments
'''
A default argument is a parameter that assumes a default value if a value is not
provided in the function call for that argument. The following example illustrates
Default arguments.
'''

def my_fun(x, y=50):
    print('x: ', x)
    print('y: ', y)

my_fun(10) # Output: x: 10 y: 50
my_fun(10, 10) # Output: x: 10 y: 10

# Docstring
'''
The first string after the function is called the Document string or Docstring in short. This is used to describe the functionality of the function. The use of docstring in functions is optional but it is considered a good practice.
'''
def even_odd(x):
    '''Function to check if the number is even or odd'''
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")

# Driver code to call the function
print(even_odd.__doc__)
even_odd(9)
        