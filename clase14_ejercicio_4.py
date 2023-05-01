ganadores=[]

contador=int(0)

while contador<10:
    ganadores.append(int(input(f"agregar {contador+1}° numero ganador: ")))
    contador=contador+1

ganadores.sort()
print(ganadores)