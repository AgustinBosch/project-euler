def triple(numa, numb):
    return((numa**2 - numb**2), (2*numa*numb), (numa**2+numb**2))


def sumar_tupla(tupla):
    return tupla[0] + tupla[1] + tupla[2]


def mult_tupla(tupla):
    return tupla[0] * tupla[1] * tupla[2]


def buscar_suma_triple(numero):
    salir = False
    i = 1
    while not salir:
        for j in range(1, i):
            suma = sumar_tupla(triple(i, j))
            if(suma == numero):
                return triple(i, j)
        i += 1


print(mult_tupla(buscar_suma_triple(1000)))
