# Python program to illustrate functions
# can be treated as objects

def shout(text):
    return text.upper()

print(shout("hello")) # HELLO

yell = shout

print(yell("world")) # WORLD

# Example 2: Passing the function as an argument 
def whisper(text):
    return text.lower()

def greet(func):
    # storing the function in a variable
    greeting = func("""Hi, I am created by a function passed as an argument""")
    print(greeting)

greet(shout) # HI, I AM CREATED BY A FUNCTION PASSED AS AN ARGUMENT
greet(whisper) # hi, i am created by a function passed as an argument

