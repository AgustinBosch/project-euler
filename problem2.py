def suma_numeros_fibo_pares_hasta(limite):
    fib = 1
    fibanterior = 1
    suma = 0
    aux = 0
    while fib <= limite:
        if(fib % 2 == 0):
            suma += fib
        aux = fib
        fib += fibanterior
        fibanterior = aux
    return suma


print(suma_numeros_fibo_pares_hasta(4000000))
