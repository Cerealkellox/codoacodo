#pedimos al usuario ingrese una letra

letra=input("ingrese una letra: ")

#chequear si es solo una letra o no
print("###########################################")
if len(letra) !=1:
    print("debe ingresar solo 1 letra")
else:
    letra=letra.lower()
    #verificamos si la letra es vocal
    
    if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
        print("la letra ingresada es una vocal")
    else:
        print("la letra ingresada no es vocal")

print("###########################################")