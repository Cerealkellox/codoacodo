frutas={"Banana":1.35, "Manzana":0.8, "Pera":0.85, "Naranja":0.7}

fruta=input("ingrese la fruta: ").title()
kg=float(input("cantidad de kilos: "))

if fruta in frutas.keys():
    valor=frutas.get(fruta)*kg
    print(f"el valortotal es {valor:.2f}")
else:
    print("no tenemos esta fruta")