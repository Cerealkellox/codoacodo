#pedir cantidad a invertir, interes anual y años
montoInversion=float(input("ingrese el monto de dinero a invertir: "))
interesInversion=float(input("ingrese el interes anual: "))
anioInversion=int(input("ingrese los años que desea calcular: "))
print("-------------------------------------------------------")
repetir=True
monto=montoInversion
anio=0

while repetir:

    print(f"capital a invertir $ {monto:0.2f}")
    inter=monto*interesInversion/100
    monto=monto+inter
    print(f"interes año {anio+1} es de ${inter:0.2f} dejando un capital de ${monto:0.2f}")
    anio+=1
    print("-------------------------------------------------------")
    if anio==anioInversion:
        repetir=False