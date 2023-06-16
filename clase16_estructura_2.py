listaNumero=[]

usuarioNumero=int(input("engrese un numero: "))
x=1
datoNumero=0

while x <= 10:
    datoNumero=datoNumero + usuarioNumero
    listaNumero.append(datoNumero)
    x+=1
print(listaNumero)