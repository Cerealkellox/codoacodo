# Pedir al usuario la cantidad de inversión, interés anual y número de años
inversion = float(input("Ingrese la cantidad a invertir: "))
interesAnual = float(input("Ingrese el interés anual (%): "))
numAnios = int(input("Ingrese el número de años de la inversión: "))
print("-------------------------------------------------------")
# Convertir el interés anual a decimal
interesDecimal = interesAnual / 100

# Calcular y mostrar el capital obtenido cada mes y año
capital = inversion
anio = 1
while anio <= numAnios:
    print("Año {}".format(anio))
    print("-------------------------------------------------------")
    for mes in range(1, 13):
        interesMensual = (capital * interesDecimal) / 12
        capital += interesMensual
        print("    Mes {}: Capital al final del mes: {:.2f}, Interés ganado: {:.2f}".format(mes, capital, interesMensual))
    interesAnual = capital - inversion
    print("-------------------------------------------------------")
    print("    Interés anual ganado: {:.2f}".format(interesAnual))
    anio += 1
    print("-------------------------------------------------------")