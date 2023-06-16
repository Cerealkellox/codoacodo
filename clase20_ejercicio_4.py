import random

lista_completa=[]
lista_pares=[]
lista_impares=[]
cant_par=int(0)
cant_inpar=int(0)
cant_numeros=int(input("cuantos numero tendra la lista: "))
i=int(0)

while i < cant_numeros:
    numer=random.randint(0,200)
    lista_completa.append(numer)
    i+=1

for valor in lista_completa:
    if valor%2==0:
        #print(f"valor {valor} divisible x 3")
        lista_pares.append(valor)
        cant_par+=1

    else:
        lista_impares.append(valor)
        cant_inpar+=1
    

print("-"*32)
print(f"{cant_numeros} numeros aleatorios")
print(lista_completa)

print("-"*32)
print(f"{cant_par} numeros pares")
print("-"*32)
print(lista_pares)
print("-"*32)
print(f"{cant_inpar} numeros inpares")
print("-"*32)
print(lista_impares)
print("-"*32)
