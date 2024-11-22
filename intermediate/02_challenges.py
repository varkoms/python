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
    for num in range(1, 101):
        if num % 5 == 0 and num % 3 == 0:
            print(f"{num} fizzbuzz")
        elif num % 3 == 0:
            print(f"{num} fizz")
        if num % 5 == 0:
            print(f"{num} buzz")
        else:
            print(num)


# fizzbuzz()

"""
¿QUÉ ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (bool) según sean o no anagrámas.
- Un anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagramas.
"""


def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())


# print(is_anagram("si", "no"))

"""
SUCESION DE FIBONACCI
Escribe un programa que imprima los 50 primeros numeros de la sucesion
de Fibonacci empezando en 0.
- La serie de Fibonacci se compone por una sucesion de numeros en
  la que el siguiente siempre es la suma de los dos anteriores.
  Ej: 0, 1, 1, 2, 3, 5, 8, 13, ...
"""


def fibonacci():

    prev = 0
    next = 1

    for index in range(0, 50):
        print(prev)
        fib = prev + next
        prev = next
        next = fib


# fibonacci()

"""
¿ES UN NUMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imrpime los números primos entre 1 y 100
"""


def is_prime():

    for number in range(1, 101):

        if number >= 2:

            is_divisible = False

            for index in range(2, number):
                if number % index == 0:
                    is_divisible = True
                    break

                if not is_divisible:
                    print(number)


# is_prime()

"""
INVIRTIENDO CADENAS A MANO
Crea un programa que invierta el orden de una cadenad de texto
SIN USAR funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo", el programa nos retornaría "odnum aloH"
"""


def reverse(text):
    text_len = len(text)
    reversed_text = ""
    for index in range(0, text_len):
        reversed_text += text[text_len - index - 1]
    return reversed_text


# print(reverse("Hola Mundo"))
