### Tuples ###

# Que es una Tuple?
'''

Contenedores para el almacenamiento de una
coleccion ordenada de uno o mas elementos
accesibles mediante indexacion.

=== Diferencia entre tuplas y listas ===
- Las tuplas SON INMUTABLES, lo que significa
que una vez creada una tupla, sus elementos
NO PUEDEN CAMBIAR.
- Las tuplas NO PUEDEN SER ALTERADAS
- No se pueden agregar, reemplazar, reasignar
 o eliminar ningun elemento, ya que las tuplas
 no pueden cambiar su configuracion
- Las tuplas tienen longitud fija
- La longitud nunca cambia a lo largo
del ciclo del programa.

'''

# Definir tuplas en Python
my_tuple = tuple()
my_other_tuple = ()

print(type(my_tuple))       # <class 'tuple'>
print(type(my_other_tuple)) # <class 'tuple'>

# Agregar elementos a la tupla
my_tuple = (33, 1.79, "Cesar", "Mendoza", "Cesar")
my_other_tuple = (35, 60, 30)
print(my_tuple) # (33, 1.79, 'Cesar', 'Mendoza')
print(my_other_tuple) # (35, 60, 30)

# Accediendo a elementos de la tupla
print(my_tuple[0]) # 33
print(my_tuple[-1]) # 'Mendoza'
# print(my_tuple[4]) # IndexError: tuple index out of range
# print(my_tuple[-6]) # IndexError: tuple index out of range

# Retorna el numero de ocurrencias del valor dado
print(my_tuple.count("Cesar")) # 2
print(my_tuple.count("Mendoza")) # 1
print(my_tuple.count("VarkoDev")) # 0

# Retorna el primer indica de la tupla del valor dado
print(my_tuple.index("Cesar")) # 2
print(my_tuple.index("Mendoza")) # 3

# Las tuplas son INMUTABLES, por ende, no se pueden reasignar valores previamente dados
# my_tuple[5] = 1.80
# print(my_tuple) # TypeError: 'tuple' object does not support item assignment

# Las tuplas pueden concatenarse
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple) # (33, 1.79, 'Cesar', 'Mendoza', 'Cesar', 35, 60, 30)

# Slices en tuplas
print(my_sum_tuple[3:6]) # ('Mendoza', 'Cesar', 35)

# Convertir una tupla en lista para poder agregar elementos
# pero esto es incoherente, ya que la tupla por definicion
# es inmutable.
#my_tuple = list(my_tuple)
#print(type(my_tuple)) # <class 'list'>
#my_tuple.insert(1, "Azul")
#my_tuple = tuple(my_tuple)
#print(my_tuple) # (33, 'Azul', 1.79, 'Cesar', 'Mendoza', 'Cesar')
#print(type(my_tuple)) # <class 'tuple'>

# No podemos eliminar elementos de una tupla
# del my_tuple[2] # TypeError: 'tuple' object doesn't support item deletion

#del my_tuple
#print(my_tuple) # NameError: name 'my_tuple' is not defined