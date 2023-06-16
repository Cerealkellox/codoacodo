datos=()

# FUNCIONES DEL PROGRAMA
def obtener_datos_personales ():
    print("ingresar datos personales: ")
    separador()
    nombre_=input("ingrese su nombre: ")
    edad_=input("ingrese su edad: ")
    ciudad_=input("ingrese su ciudad de residencia: ")
    profesion_=input("ingrese su profesion: ")

    retorno=nombre_,edad_,ciudad_,profesion_

    return(retorno)

def mostrar_informacion ():
    print("mostrado informacion del usuario")
    nombre_=datos[0]
    edad_=datos[1]
    ciudad_=datos[2]
    profesion_=datos[3]

    separador()
    print(f"Tu Nombre: {nombre_}")
    print(f"Tu Edad: {edad_}")
    print(f"Ciudad donde vives: {ciudad_}")
    print(f"Tu profesion: {profesion_}")

def separador():
    print("#"*35)

# CODIGO DEL PROGRAMA

datos=(obtener_datos_personales())
mostrar_informacion()
separador()
