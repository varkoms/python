### Dictionaries ###

# Definicion de un diccionario
my_dict = dict()
my_other_dict = {}

# Tipo de dato de un diccionario
print(type(my_dict)) # <class 'dict'>
print(type(my_other_dict)) # <class 'dict'>

# Agregando items al diccionario,
# Los valores se definen como clave:valor

my_other_dict = {"Nombre": "Cesar", "Apellido": "Mendoza", "Edad": 33, 1:"Python"}

my_dict = {
    "Nombre" : "Varko",
    "Edad": 33,
    "github": "https://github.com/varkoms",
    "lenguajes" : {"Python", "Swift", "Kotlin"},
    1: 1.79
}

print(my_other_dict) # {'Nombre': 'Cesar', 'Apellido': 'Mendoza', 'Edad': 33, 1: 'Python'}
print(my_dict) # {'Nombre': 'Varko', 'Edad': 33, 'github': 'https://github.com/varkoms', 'lenguajes': {'Python', 'Swift', 'Kotlin'}, 1: 1.79}

# Accediendo a los valores de una clave dada
print(my_dict["Nombre"]) # Varko

# Actualizar el valor de una clave dada
my_dict["Edad"] = 34
print(my_dict["Edad"]) # 34

# Imprimiendo item con clave numerica
print(my_dict[1]) # 1.79
 
# Agregando nuevo item
my_dict["Calle"] = "Calle Siempre Viva"
print(my_dict) # {'Nombre': 'Varko', 'Edad': 34, 'github': 'https://github.com/varkoms', 'lenguajes': {'Python', 'Swift', 'Kotlin'}, 1: 1.79, 'Calle': 'Calle Siempre Viva'}

# Eliminar un item de un diccionario
del my_dict["Calle"]
print(my_dict) # {'Nombre': 'Varko', 'Edad': 34, 'github': 'https://github.com/varkoms', 'lenguajes': {'Swift', 'Python', 'Kotlin'}, 1: 1.79}

# Validar si existen items en el diccionario
print("Nombre" in my_dict) # True
print(1 in my_other_dict) # True
print("Cesar" in my_other_dict) # False. Python busca por clave, no por valor (al menos en este caso)

# OPERACIONES
# items() nos devuelve un listado de cada uno de los items (clave, valor) del diccionario
print(my_dict.items()) # dict_items([('Nombre', 'Varko'), ('Edad', 34), ('github', 'https://github.com/varkoms'), ('lenguajes', {'Swift', 'Kotlin', 'Python'}), (1, 1.79)])

# keys() nos retorna un listado de las claves (keys) del diccionario
print(my_dict.keys()) # dict_keys(['Nombre', 'Edad', 'github', 'lenguajes', 1])

# values() nos retorna los valores del diccionario
print(my_dict.values()) # dict_values(['Varko', 34, 'https://github.com/varkoms', {'Swift', 'Kotlin', 'Python'}, 1.79])

# Ignore this!
# fromkeys((key1, key2, ...)) Genera un nuevo diccionario con las keys dadas, pero sin valores
#my_new_dict = my_other_dict.fromkeys(("Nombre", 1, "Genero"))
#print(my_new_dict) # {'Nombre': None, 1: None, 'Genero': None}