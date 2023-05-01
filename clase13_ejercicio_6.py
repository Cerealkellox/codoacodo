# Obtener el corrimiento
corrimiento = int(input("Ingrese el corrimiento deseado: "))

# Obtener los 5 mensajes
mensajes = []
for i in range(5):
    mensaje = input("Ingrese el mensaje {}: ".format(i+1))
    mensajes.append(mensaje)

# Encriptar los mensajes
abecedario = 'abcdefghijklmnopqrstuvwxyz'
encriptados = []
for mensaje in mensajes:
    mensajeEncriptado = ''
    for letra in mensaje:
        if letra.lower() in abecedario:
            indice = abecedario.index(letra.lower())
            letraEncriptada = abecedario[(indice+corrimiento)%len(abecedario)]
            if letra.isupper():
                letraEncriptada = letraEncriptada.upper()
            mensajeEncriptado += letraEncriptada
        else:
            mensajeEncriptado += letra
    encriptados.append(mensajeEncriptado)

# Imprimir los mensajes encriptados
print("Mensajes encriptados:")
for mensaje in encriptados:
    print(mensaje)