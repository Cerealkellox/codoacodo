#dar al usuario la eleccion del candidato

print('''
###########################################

hola sr usuario debe seleccion 1 candidato
los candidatos disponibles son:

A - candidato ROJO
B - candidato VERDE
C - candidato AZUL

###########################################
''')

candiSelecto=input("seleccione un candidato: >>> ")
candiSelecto=candiSelecto.upper()

#segun la eleccion indicar el color del partido elegido
print("###########################################")
if candiSelecto=="A":
    print("felicidades, has elegido al candidato del partido ROJO")
elif candiSelecto=="B":
    print("felicidades, has elegido al candidato del partido VERDE")
elif candiSelecto=="C":
    print("felicidades, has elegido al candidato del partido AZUL")
else:
    print("debes seleccionar un candidato")
print("###########################################")
