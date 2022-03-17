
def es_palindromo(numero):
    texto = str(numero)
    for i in range(len(texto)//2):
        if(texto[i] != texto[(i+1)*(-1)]):
            return False
    return True


def el_mayor_producto_palindromo(rango):
    mayor = 0
    for i in range(1, rango):
        for j in range(1, rango):
            if es_palindromo(i * j):
                mayor = max(i*j, mayor)
    return mayor


print(el_mayor_producto_palindromo(1000))
