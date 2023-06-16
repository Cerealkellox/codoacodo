def fizz_buzz(valor):
    if valor%3==0 and valor%5==0:
        final="fizz_buzz"
    elif valor%3==0:
        final="fizz"
    elif valor%5==0:
        final="buzz"
    else:
        final=valor
    return(final)

resu=int(input("ingrese un numero: "))
print(fizz_buzz(resu))
