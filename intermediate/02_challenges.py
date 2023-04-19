### Challenges ###

'''
FAMOSO "FIZZ BUZZ"
Escribe un programa que muestre por consola (con un print) los
numeros de 1 al 100 (ambos incluidos y con un salto de linea entre
cada impresion), sustituyendo los siguientes:
- Multiplos de 3 por la palabra "Fizz"
- Multiplos de 5 por la palabra "Buzz"
- Multiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
'''

def fizzbuzz():
    for num in range(1,101):
        if num % 5 == 0 and num % 3 == 0:
            print(f"{num} fizzbuzz")
        elif num % 3 == 0:
            print(f"{num} fizz")
        if num % 5 == 0:
            print(f"{num} buzz")
        else:
            print(num)

fizzbuzz()