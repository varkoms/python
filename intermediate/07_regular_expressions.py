### Regular Expressions ###

# Modulo re = regular expression
import re

# USO DE LA OPERACION "MATCH"
my_string = "Esta es la leccion numero 7: Leccion llamada Expresiones Regulares"
my_other_string = "Esta no es la leccion numero 6: Manejo de Ficheros"

match = re.match("Esta es la leccion", my_string, re.I)
print(match)
start, end = match.span()
print(my_string[start:end])

match = re.match("Esta no es la leccion", my_other_string)
# if not(match == None): # Otra forma de comprobar el None
# if match != None: # Una forma mas de comprobar
if match is not None:
    start, end = match.span()
    print(my_other_string[start:end])
else:
    print("Match not found")

print(re.match("Expresiones Regulares", my_string))

# USO DE LA OPERACION "SEARCH"

search = re.search("LECCION", my_string, re.I)
print(search)
start, end = search.span()
print(f'Found: "{my_string[start:end]}"')

# # USO DE LA OPERACION "FINDALL"
print(re.findall("leccion", my_string, re.I))

# USO DE LA OPERACION "SPLIT"
print(re.split(":", my_string))

# USO DE LA OPERACION "SUB"
print(f"Source: {my_string}")
print(f"New: {re.sub("Expresiones Regulares", "RegEx", my_string)}")
print(f"Another Example: {re.sub("[L|l]eccion", "LECCION", my_string)}")

# PATRONES "PATTERNS"
pattern = r'[lL]eccion'
print(re.findall(pattern, my_string))

pattern = r'[lL]eccion|Expresiones'
print(re.findall(pattern, my_string))

pattern = r'[0-9]'
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r'\d'
print(re.findall(pattern, my_string))

pattern = r'\D'
print(re.findall(pattern, my_string))

pattern = r'[l].*'
print(re.findall(pattern, my_string))

# Email Validation Regular Expression
# Ejemplo generado con ChatGPT
"""
Esta expresión regular es bastante general y cubre muchos casos comunes,
pero puede no ser 100% precisa para todos los correos electrónicos válidos
posibles según el estándar completo de direcciones de correo
(por ejemplo, direcciones que usan caracteres especiales o dominios de nivel superior muy largos).
"""
pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
email = "varkodev@example.com"
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email)) # ['varkodev@example.com']
