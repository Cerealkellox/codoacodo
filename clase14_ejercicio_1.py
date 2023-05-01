asignaturas=[]
asignaturas=list()
x=int(0)
cantMateria=int(input("ingrese la cantidad de materias a ingresar: "))

while x<cantMateria:
    asignaturas.append(input("ingresar nombre de materia: "))
    x+=1

asignaturas.sort()
print(f"la lista de materias: {asignaturas}")
