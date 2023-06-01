def draw_triforce(filas):
    if filas <= 0 :
        print("El numero de filas debe de ser un entero positivo")
        return
    
    fila_mayor = 2 * (filas - 1)

    for fila in range(1, fila_mayor + 1):
        for col in range(1, (fila_mayor * 2) + 1):
            if (fila <= filas and col >= filas - fila + 1 and col <= filas + fila - 1) or (fila > filas and col >= fila - filas + 1 and col <= fila + filas - 1):
                print("*", end="")
            else:
                print(" ", end="")
        print()

draw_triforce(5)  