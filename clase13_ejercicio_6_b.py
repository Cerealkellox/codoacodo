alfabeto = 'abcdefghijklmnopqrstuvwxyz'

corrimiento = int(input("Ingrese la cantidad de lugares a correr las letras: "))
mensaje = input("Ingrese el mensaje encriptado: ")

mensaje_descifrado = ''
for letra in mensaje:
    if letra.lower() in alfabeto:
        indice = alfabeto.index(letra.lower())
        letra_descifrada = alfabeto[(indice - corrimiento) % 26]
        if letra.isupper():
            mensaje_descifrado += letra_descifrada.upper()
        else:
            mensaje_descifrado += letra_descifrada
    else:
        mensaje_descifrado += letra
print("Mensaje descifrado:", mensaje_descifrado)