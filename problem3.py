def descomponer(numero):
    primos = []
    for i in range(2, numero + 1):
        while numero % i == 0:
            primos.append(i)
            numero /= i
        if numero == 1:
            break

    return primos


print(descomponer(600851475143))
