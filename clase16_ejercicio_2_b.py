usuario={
    "nombre":"",
    "edad":"",
    "direccion":"",
    "telefono":"",
}

usuario["nombre"]=input("ingrese su nombre: ")
usuario["edad"]=input("ingrese su edad: ")
usuario["direccion"]=input("ingrese su direccion: ")
usuario["telefono"]=input("ingrese su nro de telefono: ")

print("hola ", usuario["nombre"], " asi que tienes ", usuario["edad"], " años, vives en ", usuario["direccion"] ," y tu telefono es: ",usuario["telefono"])
