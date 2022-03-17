suma = 0
with open("suma.txt") as f:
    for i in range(100):
        suma += int(f.readline())

print(suma)
