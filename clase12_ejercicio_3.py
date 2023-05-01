#pedimos a 2 usuarios ingresen valor
valor1=input("ingrese primer valor: ")
valor2=input("ingrese segundo valor: ")

if valor1==valor2:
    print("ambos valores son iguales")
elif valor1<valor2:
    print(f"el valor mas bajo es el {valor1}")
else:
    print(f"el valor mas bajo es el {valor2}")