### Lambdas ###

"""
- Lambda es una función anónima.
- Una función lambda puede tener multiples numeros de argumentos,
pero solo puede tener una expresión

NOTE: Use lambda functions when an anonymous function is required for a short period of time.
"""

x = lambda a, b: a * b
print(x(10, 1))

# Se pueden anidar funciones lambdas dentro de otras funciones
def sum_three_values(value):
    return lambda first_value, second_value : first_value + second_value + value

print(sum_three_values(5)(5, 5))
