def divisible_por(numero, rango):
    for i in range(rango, 1, -1):
        if numero % i != 0:
            return False
    return True


def minimo_numero_divisible(numero):
    salir = False
    resultado = 0
    while(not salir):
        resultado += numero
        if divisible_por(resultado, numero):
            salir = True

    return resultado


print(minimo_numero_divisible(20))
