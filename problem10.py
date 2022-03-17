import math


def es_primo(numero, arrayprimos):
    raiz = math.sqrt(numero)
    for i in arrayprimos:
        if i > raiz:
            break
        if numero % i == 0:
            return False
    return True


suma = 0
primos = []
for i in range(2, 2000001):
    if es_primo(i, primos):
        suma += i
        primos.append(i)

print(suma)
