# Variables

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

# Cambiar tipo de dato de una variable
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable) # 5
print(type(my_int_to_str_variable)) # <class 'str'>

# Imprimir multiples variables
print(type(print(my_string_variable, my_int_to_str_variable, my_bool_variable))) # <class 'NoneType'>

# Nombres de variables no aceptados
'''
1num
first@name
first-name
firstName
first$name
num-1
!var
'''