persona={}
continuar=True

#pedimos al usuario ingrese los datos y valores
while continuar:
    clave=input("que dato quieres ingresar? ")
    valor=input(clave + ", ")
    persona[clave]=valor
    continuar=input("ingresa SI para agregar mas informacion: ").upper()=="SI" 
    
for datoPer, valorPer in persona.items():
    print("datos de la persona")
    print(datoPer, ":", valorPer)