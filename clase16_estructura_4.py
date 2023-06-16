usuarios={"martin":123456789,}
seguir=True

while seguir:

    nombre=str(input("ingrese el nombre de la persona: "))
    telefono=str(input("ingrese el telefono de la persona: "))
    
    if nombre in usuarios:
        print("el nombre ya existe en la agenda")
       
    else:
        usuarios[nombre]=telefono

    respuesta=input("desea agregar otro nombre a la agenda? SI continuar")
    
    if respuesta.upper() == "NO":
        seguir=False

print("agenda: ")

for nombre, telefono in usuarios.items():
    print(nombre, ":", telefono)

