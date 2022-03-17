def diferencia_suma_cuadrado(numero):
    suma_cuadrados = 0
    for i in range(1, numero+1):
        suma_cuadrados += i**2
    cuadrado_suma = ((numero*(numero+1))//2)**2

    return cuadrado_suma - suma_cuadrados


print(diferencia_suma_cuadrado(100))
