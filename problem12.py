import math


def cantidad_divisores(numero):
    cantidad = 0

    i = 1
    while i <= math.sqrt(numero):
        if (numero % i == 0):
            if (numero / i == i):
                cantidad += 1
            else:
                cantidad += 2
        i = i + 1
    return cantidad


def ejercicio13():
    num_triangular = 0
    contador = 1
    while True:
        num_triangular += contador
        cant_div = cantidad_divisores(num_triangular)
        if cant_div >= 500:
            break
        contador += 1
    return num_triangular


print(cantidad_divisores(76576500))
