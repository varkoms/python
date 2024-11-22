"""
Expresiones Regulares en Python

NOTA: Esto no es parte del curso intermedio de Python de @mouredev, esto
fue parte del directo en Twitch sobre aprendiendo Expresiones Regulares
desde cero.
"""

import re

# Expresion regular para validar una URL
regex = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
findall = ' '.join(re.findall(regex, "http://www.varkode.com/"))
print(findall)
