from math import *

# Pedimos al usuario que ingrese la fecha
fecha = input("Ingrese la fecha en formato 'día, DD/MM': ")

# Validamos que la fecha tenga el formato correcto
if "," not in fecha or "/" not in fecha:
    print("##################################")
    print("Error: formato de fecha incorrecto.")
    print("##################################")
    exit()

# Separamos el nombre del día, el número de día y el número de mes
nombreDia, fechaMes = fecha.split(", ")
numDia, numMes = fechaMes.split("/")

#print(nombreDia)
#print(numDia)
#print(numMes)

# Validamos que el día y el mes sean números válidos
if not numDia.isdigit() or not numMes.isdigit() or int(numDia) > 31 or int(numMes) > 12:
    print("##################################")
    print("Error: fecha inválida.")
    print("##################################")
    exit()

# Convertimos el nombre del día a minúsculas para simplificar la validación
nombreDia = nombreDia.lower()

# Validamos si se tomaron exámenes
if nombreDia == "lunes" or nombreDia == "martes" or nombreDia == "miércoles":
    examenes = input("¿Se tomaron exámenes? (s/n): ")
    if examenes.lower() == "s":
        aprobados = int(input("Ingrese la cantidad de alumnos aprobados: "))
        desaprobados = int(input("Ingrese la cantidad de alumnos desaprobados: "))
        porcentajeAprobados =  aprobados * 100 / (aprobados + desaprobados) 
        print("##################################")
        print(f"El porcentaje de aprobados fue del {trunc(porcentajeAprobados)}%")
        print("##################################")

# Validamos si es práctica hablada
elif nombreDia == "jueves":
    print("##################################")
    asistencia = int(input("Ingrese el porcentaje de asistencia a la clase: "))
    if asistencia > 50:
        print("Asistió la mayoría.")
    else:
        print("No asistió la mayoría.")
    print("##################################")

# Validamos si es inglés para viajeros
elif nombreDia == "viernes" and (numMes == "1" or numMes == "7") and numDia == "1":
    print("Comienzo de nuevo ciclo.")
    alumnos = int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
    arancel = float(input("Ingrese el arancel en $ por cada alumno: "))
    ingresoTotal = alumnos * arancel
    print("El ingreso total es de $", ingresoTotal)