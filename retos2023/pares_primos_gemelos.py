def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def encontrar_pares_primos_gemelos(rango_maximo):
    pares_gemelos = []
    for num in range(2, rango_maximo - 1):
        if (is_prime(num) and is_prime(num + 2)):
            pares_gemelos.append((num, num + 2))
    return pares_gemelos

print(encontrar_pares_primos_gemelos(14))
print(encontrar_pares_primos_gemelos(21))