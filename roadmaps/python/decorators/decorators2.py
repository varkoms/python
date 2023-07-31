# Assigning Functions to Variables

# To kick us off we create a function that will add one to a number whenever it is called. We'll then assign the function to a variable and use this variable to call the function.

def plus_one(number):
    return number + 1

add_one = plus_one
print(add_one(5)) # 6

# Defining Functions inside other Functions
def plus_one(number):
    def add_one(number):
        return number + 1
    
    result = add_one(number)
    return result

print(plus_one(4)) # 5

# Passing functions as arguments to other functions
# Functions can also be passed as parameters to other functions. 

def plus_one(number):
    return number + 1

def function_call(function):
    number_to_add = 5
    return function(number_to_add)

print(function_call(plus_one)) # 6

# Functions returning other functions
def hello_function():
    def say_hi():
        return "Hi"
    return say_hi

hello = hello_function()
print(hello()) # Hi

# Nested functions have access to the Enclosing
# Function's variable scope

def print_message(message):
    "Enclosing function"
    def message_sender():
        "Nested Function"
        print(message)

    message_sender()

print_message("Some random message") # Some random message