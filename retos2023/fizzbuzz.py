"""
Escribe un programa que muestre por consola (print) los
numeros del 1 al 100 (ambos incluidos y con un salto de linea entre
cada impresion), sustituyendo los siguientes:

- Multiplos de 3 por la palabra "fizz"
- Multiplos de 5 por la palabra "buzz"
- Multiplos de 3 y de 5 a la vez por la palabra "fizzbuzz"
"""

def fizzbuzz():

    for number in range(1, 101):
        if number % 3 == 0:
            print(f"{number} fizz")
        elif number % 5 == 0:
            print(f"{number} buzz")
        elif number % 3 == 0 and number % 5 == 0:
            print(f"{number} fizzbuzz")
        else:
            print(f"{number}")

fizzbuzz()