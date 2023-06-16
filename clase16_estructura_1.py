mesAnio=("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")

eleccion=int(input("ingrese el numero del mes: "))

if eleccion>=1 and eleccion < len(mesAnio):
    print(f"has seleccionado el mes de {mesAnio[eleccion-1]}")
else:
    print("fuera de los meses")
