# Solicita al usuario que ingrese un año
anio = int(input("Ingrese un año: >>> "))

# Verifica si el año es bisiesto
print("###########################################")
if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
    print(anio, "es un año bisiesto.")
else:
    print(anio, "no es un año bisiesto.")
print("###########################################")