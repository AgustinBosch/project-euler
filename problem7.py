def divisible_por_alguno(numero, array):
    for i in array:
        if numero % i == 0:
            return True
    return False


def nte_primo(number):
    primos = []
    pri = 2
    while len(primos) < number:
        if not divisible_por_alguno(pri, primos):
            primos.append(pri)
        pri += 1

    return primos


print(nte_primo(10001)[-1])
