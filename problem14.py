def pasos_collatz_de(numero):
    pasos = 1
    while numero != 0:
        if numero == 1:
            return pasos
        if numero % 2 == 0:
            numero /= 2
        else:
            numero = numero*3+1
        pasos += 1


numero = 0
mayor_cadena = 0
for i in range(1, 1000000):
    aux = pasos_collatz_de(i)
    if(aux > mayor_cadena):
        numero = i
        mayor_cadena = aux

print(numero, mayor_cadena)
