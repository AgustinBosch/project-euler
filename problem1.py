def sumarMultiplosTresCincoHasta(numero):
    suma = 0
    for i in range(1, numero):
        if(i % 3 == 0 or i % 5 == 0):
            suma += i
    return suma


print(sumarMultiplosTresCincoHasta(1000))
