### Higher Order Functions ###

from functools import reduce

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_add_value(first_value, second_value, fn):
    return fn(first_value + second_value)

print(sum_two_values_and_add_value(5, 2, sum_one))
print(sum_two_values_and_add_value(5, 2, sum_five))

### Closures ###
def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add
    
add_closure = sum_ten(5)
print(add_closure(5))

# otra forma de llamar a las closures, usando el tipo de llamado lambda
print(sum_ten(5)(5)) # 20


### Built-in Higher Order Functions ###

# Map
numbers = [2, 5, 10, 21, 3, 30]

def multiply_by_two(number):
    return number * 2

print(list(map(multiply_by_two, numbers))) # [4, 10, 20, 42]
print(list(map(lambda number : number * 2, numbers))) # [4, 10, 20, 42]

# Filter
def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_than_ten, numbers))) # [21, 30]
print(list(filter(lambda number : number > 10, numbers))) # [21, 30]

# Reduce (se necesita importar la libreria functools (linea 3) para usar reduce)

def sum_two_values(first_value, second_value):
    return first_value + second_value

print(reduce(sum_two_values, numbers)) # 71
print(reduce(lambda first_value, second_value: first_value + second_value, numbers)) # 71