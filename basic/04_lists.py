### Lists ###

my_list = list()
my_other_list = []

# Tipo de Dato de una lista
print(type(my_list)) # <class 'list'>
print(type(my_other_list)) # <class 'list'>

# Imprimir la longitud de la lista
print(len(my_list)) 

# Agregar elementos a la lista
my_list = [35, 24, 62, 52, 30, 30, 17]
print(my_list) # [35, 24, 62, 52, 30, 30, 17]
print(len(my_list)) # 7

# Agregar diferentes tipos de datos en una lista
my_other_list = [35, 1.77, "Cesar", "Mendoza"]

print(type(my_other_list))

# Acceder a los elementos de la lista
print(my_other_list[0]) # 35
print(my_other_list[1]) # 1.77
print(my_other_list[-1]) # "Mendoza"
print(my_other_list[-3]) # 1.77
print(my_other_list[-4]) # 35
# print(my_other_list[-5]) # IndexError: list index out of range
# print(my_other_list[4]) # IndexError: list index out of range

# Retorna el numero de coincidencias del valor ingresado como parametro
print(my_other_list.count("Mendoza")) # 1
print(my_list.count(30)) # 2

# Desempaquetar variables de una lista
age, height, name, surname = my_other_list
print(age) # 35
print(height) # 35
print(name) # "Cesar"
print(surname) # "Mendoza"

# "Sumar" listas, en realidad las listas se concatenan
print(my_list + my_other_list) # [35, 24, 62, 52, 30, 30, 17, 35, 1.77, 'Cesar', 'Mendoza']
# print(my_list - my_other_list) # unsupported operand type(s) for -: 'list' and 'list'
# print(my_list * my_other_list) # can't multiply sequence by non-int of type 'list'


# Tipos dinamicos
# my_list = "Hola Python"
# print(my_list) # Hola Python
# print(type(my_list)) # <class 'str'>

# Operaciones con los elementos

# append(item) inserta un nuevo elemento AL FINAL de la lista
my_other_list.append('VarkoDev')
print(my_other_list) # [35, 1.77, 'Cesar', 'Mendoza', 'VarkoDev']

# insert(idx) indica el indice e inserta un nuevo elemento a la lista en esa posicion
my_other_list.insert(1, "Negro")
print(my_other_list) # [35, 'Negro', 1.77, 'Cesar', 'Mendoza', 'VarkoDev']

# Actualizamos el segundo elemento de la lista
my_other_list[1] = "Rojo"
print(my_other_list) # [35, 'Rojo', 1.77, 'Cesar', 'Mendoza', 'VarkoDev']

# remove(item) elimina el item especificado de la lista,
# siempre y cuando conozcamos el elemento se encuentra en la lista
# Si existen mas coincidencias, solo elimina una de ellas.
my_other_list.remove("Rojo")
print(my_other_list) # [35, 1.77, 'Cesar', 'Mendoza', 'VarkoDev']

# Valores originales
print(my_list)

# pop(idx?) Si no se indica un elemento idx, elimina y retorna el ultimo valor desapilado de la lista.

print(my_list.pop()) # 17
print(my_list) # [35, 24, 62, 52, 30, 30]

# Pero para pop() lo mas comun es usarlo sin parametros, para que siempre desacople el ultimo elemento de la lista.
# Se puede pasar un parametro, pero no es lo recomendado.
# print(my_list.pop(2)) # 62
# print(my_list) # [35, 24, 52, 30, 30]

# Para eliminar un elemento de la lista por indice usar la siguiente forma
del my_list[2]
print(my_list) # [35, 24, 52, 30, 30]

# copy() Hace una copia superficial de una lista
my_new_list = my_list.copy()
print(my_new_list) # [35, 24, 52, 30, 30]

# reverse() Devuelve la lista con los elementos invertidos
my_new_list.reverse()
print(my_new_list) # [30, 30, 52, 24, 35]

# sort() ordena los elementos de la lista del menor a mayor, este orden es por defecto
my_new_list.sort()
print(my_new_list)

# Ordenar los elementos de la lista pero de mayor a menor
my_new_list.sort(reverse=True)
print(my_new_list) # [52, 35, 30, 30, 24]

# clear() Elimina todos los elementos de lista, NO elimina la lista como tal.
my_list.clear()
my_new_list.clear()
print(my_list) # []
print(my_new_list) # []