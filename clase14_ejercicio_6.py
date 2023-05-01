materias=["matematica","lengua","ingles","fisica","biologia", "geografia","ciudadania","quimica","artistica"]
notas=[]

#pedimos al usuario ingresar las notas de las materias
for materia in materias:
    nota=int(input(f"que nota has sacado en {materia}: "))
    notas.append(nota)

#chequear las materias mayores a 5 y eliminarlas de la lista
i=int(0)
while i < len(notas):
    if notas[i] >= 5:
        notas.pop(i)
        materias.pop(i)
    else:
        i+=1

#mostrar cada una de las materias que quedaron por rendir
print("######################################")
print("debes rendir las siguientes materias: ")
for materia in materias:
    print(materia)
