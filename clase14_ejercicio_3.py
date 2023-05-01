materias=["matematica","lengua","ingles","fisica","biologia"]
notas=[]

for materia in materias:
    nota=float(input(f"que nota has sacado en {materia}: "))
    notas.append(nota)

#print(notas)

for i in range(len(materias)):
    print(f"en {materias[i]} has sacado {notas[i]}")
    print
