divisa={
    "euro":"€",
    "dolar":"$",
    "yen":"¥"
}

pago=str(input("en que divisa desea pagar?: "))

if pago in divisa.keys():
    eleccion=divisa.get(pago)
    print(f"usted eligio la divisa {eleccion}")
else:
    print("metodo elegido no valido")
