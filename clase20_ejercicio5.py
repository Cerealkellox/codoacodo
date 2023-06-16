def menu_sumar(num1,num2):
    resu=num1+num2
    return(resu)

def menu_resta(num1,num2):
    resu=num1-num2
    return(resu)

def menu_multiplicar(num1,num2):
    resu=num1*num2
    return(resu)

def menu_dividir(num1,num2):
    resu=num1/num2
    return(resu)

def separador():
    print("-"*32)


repetir=True

while repetir==True:
    separador()
    print("\tmenu \n(1)suma \n(2)resta \n(3)multiplicacion \n(4)division \n(5)salir")
    separador()
    eleccion=int(input("ingresar seleccion: "))
    
    if eleccion==5:
        break
    
    separador()
    print("ingresar dos numeros:")
    numero1=int(input("numero el primer numero: "))
    numero2=int(input("ingrese el segundo numero: "))
    separador()

    if eleccion==1:
        print(f"resultado de la suma: { menu_sumar(numero1,numero2)}")
    elif eleccion==2:
        print(f"resultado de la resta: { menu_resta(numero1,numero2)}")
    elif eleccion==3:
        print(f"resultado de la multiplicacion: { menu_multiplicar(numero1,numero2)}")
    elif eleccion==4:
        print(f"resultado de la division: { menu_dividir(numero1,numero2)}")
    else:
        print("debes elegir 1,2,3,4 o 5")
    separador()