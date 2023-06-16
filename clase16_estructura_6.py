lista=[]
suma=int

inicio=int(0)

while inicio < 10:
    dato=int(input("agrege un valor"))
    lista.insert(inicio, dato)
    inicio+=1

finlista=len(lista)
suma=sum(lista)
media=suma/finlista
print(f"la suma de los valores de la lista es {suma} y la media es {media:0.2f}")