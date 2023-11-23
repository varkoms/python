import random

rupiasEnCofres = [10, 15, 20, 25]


def calcular_numero_aleatorio_entre(minimo, maximo):
    return random.randint(minimo, maximo)


def abrir_cofre_de_rupias():
    numero_aleatorio = calcular_numero_aleatorio_entre(0, 3)
    rupias_obtenidas = rupiasEnCofres[numero_aleatorio]
    return rupias_obtenidas


print(f"Link encontró un tesoro con {abrir_cofre_de_rupias()} rupias")
