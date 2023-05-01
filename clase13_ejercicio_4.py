#le pedimos al usuario que ingrese 6 numeros enteros, positivo o negativos
numeroPosi=0
numeroNega=0
numeroDato=0
repite=0
contadorPosi=0

while repite<6:
    numeroDato=int(input("Ingrese un numero: "))
    if numeroDato<0:
        numeroNega=numeroNega+numeroDato
        repite+=1
    elif numeroDato>0:
        numeroPosi=numeroPosi+numeroDato
        repite+=1
        contadorPosi+=1
    else:
        print("debe ingresar un numero")


numeroPosi=numeroPosi/contadorPosi
print(f"la suma de los negativos es: {numeroNega}, y el promedio de los positivos es: {numeroPosi}")