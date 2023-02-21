### Sets ###

'''
Sets son usados para almacenar
multiples items en una sola variable

Un set es una coleccion de datos
desordenados, inmutables,
no estan indexados y tampoco permiten
datos repetidos

NOTA: Si bien los sets son inmutables,
se permiten eliminar y agregar nuevos items
'''

# Definiendo sets
my_set = set()
my_other_set = {}

# Tipo de dato del set
print(type(my_set)) # <class 'set'>
print(type(my_other_set)) # <class 'dict'> Inicialmente se define como un diccionario

# Agregando items al set
my_other_set = {"Cesar", "Mendoza", 33}

# Imprimiendo my_other_set
print(my_other_set) # {33, 'Cesar', 'Mendoza'}
print(type(my_other_set)) # <class 'set'>

# Longitud del length
print(len(my_other_set)) # 3

# Un set no tiene indices, por lo tanto la siguiente linea tira error.
# print(my_other_set[0]) # TypeError: 'set' object is not subscriptable

# Agregando un nuevo item a un set existente
my_other_set.add("VarkoDev")

# Al no ser una estructura ordenada, el print 
# tendra diferentes comportamientos a la hora
# de mostrar los items
print(my_other_set) # {33, 'Cesar', 'Mendoza', 'VarkoDev'} , {'Mendoza', 33, 'VarkoDev', 'Cesar'}, {33, 'VarkoDev', 'Cesar', 'Mendoza'}

# Busquedas en sets
print("VarkoDev" in my_other_set) # True
print("Varkinio" in my_other_set) # False

# Removiendo items individuales del set
my_other_set.remove("VarkoDev")
print(my_other_set) # {33, 'Mendoza', 'Cesar'}

# Elimina por completo los items del set
my_other_set.clear()
print(my_other_set) # set()
print(len(my_other_set)) # 0

# Eliminar el set por completo
# del my_other_set
# print(my_other_set) # NameError: name 'my_other_set' is not defined

my_set = {"Cesar", "Mendoza", 33}
my_other_set = {"Python", "JS", "Java"}
my_new_set = my_set.union(my_other_set)
print(my_new_set) # Comportamiento variable => {'Python', 33, 'Mendoza', 'Java', 'Cesar', 'JS'}, {33, 'Python', 'Java', 'Cesar', 'JS', 'Mendoza'}, etc

# Al no permitir datos repetidos, la siguiente operacion
# solo regresa el contenido del set my_new_set
print(my_new_set.union(my_new_set))

# A menos que meta un nuevo item al set, ahi si se podrian
# agregar items al set
print(my_new_set.union({"C#", "Swift"})) # {'C#', 33, 'JS', 'Python', 'Cesar', 'Mendoza', 'Java', 'Swift'}

# Retorna la diferencia entre dos o mas sets como un nuevo set
print(my_new_set)
print(my_set)
print(my_new_set.difference(my_set)) # {'Java', 'Python', 'JS'}