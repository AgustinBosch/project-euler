def es_bisiesto(anio):
    return (anio % 400 == 0) if (anio % 100 == 0) else (anio % 4 == 0)


def dias_del_mes(mes, anio):
    meses = [31,  29 if es_bisiesto(anio) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return meses[mes - 1]

cantidad_dias = 0
cantidad_domingos = 0
for anio in range(1901,2001):
    for mes in range(1,13):
        if cantidad_dias % 7 == 0:
            cantidad_domingos += 1
        cantidad_dias += dias_del_mes(mes, anio)


print(cantidad_dias)
print(cantidad_domingos)
