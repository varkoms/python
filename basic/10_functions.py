### Functions ###

# Function without parameters
def my_function():
    print("Esto es una funcion")

# Function with two parameters
def sum_two_values(first_number, second_number):
    print(first_number + second_number)

# Function with return
def sum_two_values_with_return(first_value, second_value):
    my_result = first_value + second_value
    return my_result

def print_name(name, surname):
    print(f"{name} {surname}")

def print_name_with_default(name, surname, alias="Sin Alias"):
    print(f"{name} {surname} {alias}")

def print_texts(*texts):
    for text in texts:
        print(text)

# Calling functions
my_function() # Esto es una funcion
sum_two_values(5, 7) # 30
sum_two_values(12300, 4560) # 16860
sum_two_values("12300", "4560") # 123004560
sum_two_values(1.4, 5.2) # 6.6

my_result = sum_two_values_with_return(10, 5)
print(my_result) # 15

print_name(surname="Mendoza", name="Cesar") # Cesar Mendoza
print_name_with_default("Cesar", "Mendoza", "Varko") # Cesar Mendoza Varko
print_name_with_default("Cesar", "Mendoza") # Cesar Mendoza Sin Alias

print_texts("Hola", "Python", "VarkoDev") # ('Hola', 'Python', 'VarkoDev')
print_texts("Hola") # ('Hola',)