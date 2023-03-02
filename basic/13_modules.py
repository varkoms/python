### Modules ###

# Importar todo el modulo
# import module
# module.sum_two_values(10, 20) # 30

# Importar funciones concretas
from module import sum_two_values, my_function

sum_two_values(10, 20) # 30
my_function() # Esto es una funcion

# Modulos de sistema
import math
print(math.pi) # 3.141592653589793

# Importar modulos y renombrar propiedades
from math import pi as PI_VALUE
print(PI_VALUE) # 3.141592653589793