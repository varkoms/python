"""
Escribe un programa que reciba un texto y transforma lenguaje natural a
"lenguaje hacker" (conocido como "leet" o "1337"). Este lenguaje
se caracteriza por sustituir caracteres alfanumericos.

> Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
  con el alfabeto y los numeros en "leet"
> Usa la primera opcion de cada transformacion. Por ejemplo "4" para la "a"

"""

def leet_translator(text: str):
    leet = {"A": "4", "B": "I3", "C": "[", "D": ")", "E": "3", "F": "|=", "G": "&", "H": "#", "I": "1",
            "J": ",_|", "K": ">|", "L": "1", "M": "/\/\\", "N": " ^/", "O": "0", "P": " |*", "Q": "(_,)",
            "R": "I2", "S": "5", "T": "7", "U": "(_)", "V": "\/", "W": "\/\/", "X": "><", "Y": "j", "Z": "2",
            "1": "L", "2": "R", "3": "E", "4": "A", "5": "S", "6": "b", "7": "T", "8": "B", "9": "g", "0": "o"}
    
    leet_text = ""

    for word in text:
        if word.upper() in leet.keys():
            leet_text += leet[word.upper()]
        else:
            leet_text += word
        
    return leet_text

print(leet_translator("Leet"))
print(leet_translator("Aquí está un texto de prueba para ver si funciona el reto!"))
print(leet_translator(input("Ingresa el texto a traducir: ")))