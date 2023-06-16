curso={
"matematicas":6,
"fisica":4,
"quimica":5,
"lengua":7,
"biologia":9,
}
suma_notas=0
for materia, nota in curso.items():
    print("en ", materia, " tiene: ", nota)
    suma_notas +=nota
print("promedio del alumno: ", suma_notas/len(curso))
