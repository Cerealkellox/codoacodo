materias=[]
materias=list()
contador=0


cantMateria=int((input("Cuantas materia tengo que cursar? ")))

while contador<cantMateria:
    materia=str(input("ingrese las materias que cursare este semestre: "))
    materias.append(materia)
    contador+=1

contador=0

for materia in materias:
    print(f"{contador+1}° materia a estudiar: {materias[contador]}")
    contador+=1

#while contador<cantMateria:
#    print(f"{contador+1}° materia a estudiar: {materias[contador]}")
#    contador+=1
    