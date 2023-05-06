### Error Types ###
##  NOTA: Descomentar las lineas para poder obtener los errores

# Syntax Error
# print "Hola Comunidad" # SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?

# Name Error
# print(language) # NameError: name 'language' is not defined

# Index Error
my_list = ["Python", "Swift", "Kotlin", "Dart", "R", "JavaScript"]
print(my_list[0]) # Python
# print(my_list[10]) # IndexError: list index out of range

# Module Not Found Error
# import maths # ModuleNotFoundError: No module named 'maths'
import math

# Attribute Error
# print(math.PI) # AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
print(math.pi) # 3.141592653589793

# Key Error
my_dict = {"Nombre": "Varko", "Apellido": "MS", "Edad": 34, 1: "Python"}
print(my_dict["Nombre"]) # Varko
# print(my_dict["Genero"]) # KeyError: 'Genero'

# Type Error
# print(my_list["Genero"]) # TypeError: list indices must be integers or slices, not str

# Import Error
# from math import PI # ImportError: cannot import name 'PI' from 'math' 

# Value Error
# my_int = int("10 años")
# print(my_int) # ValueError: invalid literal for int() with base 10: '10 años'

# Zero Division Error
# print(4 / 0) # ZeroDivisionError: division by zero