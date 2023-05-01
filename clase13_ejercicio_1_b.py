#pedir cantidad a invertir, interes anual y años
montoInversion=float(input("ingrese el monto de dinero a invertir: "))
interesInversion=float(input("ingrese el interes anual: "))
anioInversion=int(input("ingrese los años que desea calcular: "))

repetir=True
capital=montoInversion
anio=0
capitalMensual=0
mes=0

while repetir:

    print("-------------------------------------------------------")
    print(f"capital a invertir $ {capital:0.2f}")

    interAnual=capital*interesInversion/100
    interMensual=interAnual/12
    capital=capital+interMensual
    capitalMensual=capitalMensual+interMensual
        
    print(f"interes mes {mes+1} es de ${interMensual:0.2f} dejando un capital de ${capital:0.2f}")
    mes+=1
    
    if mes == 12:
        anio+=1
        print("###################################")
        print(f"durante el año {anio} se obtuvo ${capitalMensual:0.2f} en interes")
        print("###################################")
        mes=0
        interMes=0


    if anio==anioInversion:
        repetir=False