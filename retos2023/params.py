"""
Dada una URL con parametros, crea una funcion que obtenga sus valores
    - No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.

Ejemplo: De la URL https://retosdeprogramacion.com?year=2023&challenge=0
los parametros serian ["2023", "0"]
"""


# Usando expresiones regulares
import re

url = "https://retosdeprogramacion.com?year=2023&challenge=11&languaje=javascript"

regex = r"=([a-zA-Z0-9._%-]+)"
params = re.findall(regex, url)
print(params)