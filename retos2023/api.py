"""
Implementar un llamado HTTP a una API (la que sea)
y muestra su resultado a traves de la terminal.

NOTAS: Se debe de instalar la libreria "requests"
Ingresar en terminal: pip3 install requests
"""

import requests

url = "https://rickandmortyapi.com/api/character/1,183"

response = requests.get(url)

for index, character in enumerate(response.json()):
    character_name = character["name"]
    print(f"#{index + 1} {character_name}")