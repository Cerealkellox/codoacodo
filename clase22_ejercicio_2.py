alumnos={}



def separador():
    print("#"*35)

def separador2(texto):
    print(f"******** {texto} ********")

def registrar_alumno():
    separador2("AGREGAR ALUMNO")
    nombre_=input("ingese nombre del alumno ==> ")
    dni_=input("ingese dni del alumno ==> ")
    legajo_=input("ingese legajo del alumno ==> ")
    promedio_=input("ingese promedio del alumno ==> ")
    alumnos[dni_]=nombre_,legajo_,promedio_
    separador2("ALUMNOS AGREGADO")

def mostrar_informacion():
    separador2("DATOS DEL ALUMNO")
    dato=input("ingrese DNI del alumno ==> ")
    mostrar_dato(dato)

def mostrar_dato(dni):
    
    lista=alumnos[dni]
    
    print(f"Nombre: {lista[0]}")
    print(f"DNI: {dni}")
    print(f"Legajo: {lista[1]}")
    print(f"Promedio: {lista[2]}")

def menu_principal():
      
    seguir=True
    while seguir==True:
        separador2("MENU ALUMNOS")
        eleccion=int(input("Elegir opcion para continuar:\n[1]Registrar alumno\n[2]mostrar alumnos\n[0]salir\nSeleccionar Opcion ==> "))

        if eleccion==1:
            registrar_alumno()
        elif eleccion==2:
            mostrar_informacion()
        elif eleccion==0:
            separador2("SALIENDO DEL PROGRAMA")
            quit()
        else:
            print("Lo siento opcion no valida\nSeleccionar un opcion valida")


#######################################################
menu_principal()
