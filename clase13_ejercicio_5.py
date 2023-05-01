# Pedir al usuario que ingrese los dos años
año1 = int(input("Ingrese el primer año: "))
año2 = int(input("Ingrese el segundo año: "))

# Iterar sobre los años en el rango especificado
for año in range(año1, año2 + 1):
    # Comprobar si el año es bisiesto y múltiplo de 10
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0) and año % 10 == 0:
        print(año)