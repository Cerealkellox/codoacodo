nota = float(input("Ingrese la nota de su examen: "))

if nota < 0 or nota > 10:
    print("La nota ingresada es inválida")
else:
    if nota <= 3:
        print("Examen desaprobado")
    elif nota <= 4.99:
        print("Debe recuperar el examen")
    elif nota <= 6.99:
        print("Bastante flojo, pero aprobaste")
    elif nota <= 8.99:
        print("As aprobado el examen")
    elif nota <=10:
        print("Aprobas con honores el examen")
    else:
        print("Ingresaste mal la nota")