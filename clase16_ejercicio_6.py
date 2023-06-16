compra={}
continuar=True
total=0

while continuar:
    producto=input("que dato quieres ingresar? ")
    precio=float(input(f"ingrese el precio de: {producto}: "))
    total=total+precio
    compra[producto]=precio

    continuar=input("Agregar producto? (SI/NO): ").upper()=="SI"

print("#####################")
print("compra realizada")

for prod, val in compra.items():
    #print(" $", val," - ", prod)
    print(f"$ {val:.2f} - {prod}")

print("#####################")
print(f"total: ${total}")