### File Handling ###

import os
import json
import csv

# MANEJO DE ARCHIVOS TXT

txt_file = open("my_file.txt", "w+") # Abrir el archivo en modo escritura plus

# print(txt_file.read())
# print(txt_file.read(10)) # Lee solo los primeros 10 caracteres del archivo
# print(txt_file.readline()) # Lee linea por linea el archivo
# print(txt_file.readline()) # Lee linea por linea el archivo

#print(txt_file.readlines()) # Retorna una lista de cada linea del archivo separada por comas.

txt_file.write("Hola, me llamo Varko\nAmo el desarrollo de software!\nTrabajo como QA analyst\ny me encanta el cafe")

# Se puede iterar sobre cada linea e imprimirlas de manera legible
for line in txt_file.readlines():
    print(line)

# Escribir dentro del archivo
txt_file.write("\nEstoy aprendiendo Python")

txt_file.close()

# Eliminar el archivo del sistema.
# os.remove("my_file.txt")

# MANEJANDO ARCHIVOS JSON
json_file = open("my_file.json", "w+")

json_text = {
    "nombre": "VarkoMS",
    "surnamne": "Varkito",
    "edad" : 34,
    "languages": ["Python", "JavaScript", "Swift"],
    "website" : "https://varkode.me"
}

json.dump(json_text, json_file, indent=2)

json_file.close()

with open("my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)


# ARCHIVOS CSV
