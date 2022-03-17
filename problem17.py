import inflect

p = inflect.engine()
suma = 0

for i in range(1,1001):
    suma += len(p.number_to_words(i).replace(",","").replace(" ","").replace("-",""))

print(suma)
