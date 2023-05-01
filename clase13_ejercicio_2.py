#pedir al usuario ingrese una frase y una letra
userFrase=str(input("ingrese una frase que le guste: "))
userLetra=str(input("ahora, ingrese una letra: "))

contador=0

for buscarLetra in userFrase:
    if buscarLetra==userLetra:
        contador+=1

print(f"el caracter {userLetra} aparece {contador} veces en la frase")
