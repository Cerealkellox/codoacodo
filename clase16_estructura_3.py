listaNumeros=[]
numer=1
print("ingrese 0 para dejar de pedirle numeros")
while numer != 0:
    numer=int(input("ingrese un numero: "))
    if numer not in listaNumeros:
        listaNumeros.append(numer)

listaNumeros.sort()

print(listaNumeros)