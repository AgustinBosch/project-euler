import math

# The number of paths are the central binomial coefficients


def binomial_coefficients(numero):
    return int(math.factorial(2*numero)/math.factorial(numero)**2)


print(binomial_coefficients(20))
