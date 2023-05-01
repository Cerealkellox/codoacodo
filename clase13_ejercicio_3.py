numeroUno=0
numeroDos=1
contador=0


while contador<12:
    print(F"{numeroUno}")
    proximo=numeroUno+numeroDos
    numeroUno=numeroDos
    numeroDos=proximo
    contador+=1

