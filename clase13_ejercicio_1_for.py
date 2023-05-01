# Pedir al usuario la cantidad de inversión, interés anual y número de años
inversion = float(input("Ingrese la cantidad a invertir: "))
interesAnual = float(input("Ingrese el interés anual (%): "))
numAnios = int(input("Ingrese el número de años de la inversión: "))
print("-------------------------------------------------------")
# Convertir el interés anual a decimal
interesDecimal = interesAnual / 100

# Calcular y mostrar el capital obtenido cada año
capital = inversion
for i in range(numAnios):
    capital += capital * interesDecimal
    print("Capital después del año {}: {:.2f}".format(i+1, capital))
    print("-------------------------------------------------------")