materias=["matematicas","fisica","quimicca","historia","lengua"]
notas=[]
for materia in materias:
    nota=input(f"ingrese la nota que se saco en {materia}: ")
    notas.append(nota)

for i in range(len(materias)):print(f"en {materias[i]} has sacado :{notas[i]}")