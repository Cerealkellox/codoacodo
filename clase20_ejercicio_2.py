def convertir_notas(diccionario_notas):
    diccionario_calificaciones = {}

    for materia, nota in diccionario_notas.items():
        materia_mayusculas = materia.upper()
        calificacion = obtener_calificacion(nota)
        diccionario_calificaciones[materia_mayusculas] = calificacion

    return diccionario_calificaciones

def obtener_calificacion(nota):
    if nota >= 90:
        return "A"
    elif nota >= 80:
        return "B"
    elif nota >= 70:
        return "C"
    elif nota >= 60:
        return "D"
    else:
        return "F"

# Ejemplo de uso
notas_alumno = {"matemáticas": 85, "física": 92, "química": 78, "historia": 65}

calificaciones_alumno = convertir_notas(notas_alumno)

for materia_alumno, nota_alumno in calificaciones_alumno.items():
    print(f"para la materia: {materia_alumno} la nota fue: {nota_alumno}")