compra={}
continuar=True
total=0
print("cargar los datos de la compra")
print("para finalizar escribir (FIN)")
print("-----------------------------")

while continuar:
    producto=input("agregar producto: ").upper()
    if producto=="FIN":
        break    
    precio=float(input(f"precio de {producto}: "))
    total=total+precio
    compra[producto]=precio

#nos muestra la lista de compra y precio final
print("#####################")
print("compra realizada")
print("#####################")

for prod, val in compra.items():
    #print(" $", val," - ", prod)
    print(f"$ {val:.2f} - {prod}")

print("#####################")
print(f"total: ${total:.2f}")
print("#####################")