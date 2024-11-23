# Tipado Dinamico

my_string_variable = "My String Variable"
print(my_string_variable)
print(type(my_string_variable)) # <class 'str'>

my_string_variable = 5
print(my_string_variable)
print(type(my_string_variable)) # <class 'int'>

# Type Hints
"""
INFORMACION DEL SITIO WEB DE FAST API
Los type hints son una nueva sintaxis desde Python 3.6+
que permite declarar el tipo de una variable.

Usando declaraciones de tipos para las variables, los editores
y otras herramientas pueden proveerte un soporte mejor
"""

my_typed_variable: str = "My typed String variable"
print(my_typed_variable)
print(type(my_typed_variable))

my_typed_variable = 5
print(my_typed_variable)
print(type(my_typed_variable))
