import random

def recortar(numero, minimo, maximo):
    if numero < minimo:
        return f"minimo {minimo}"
    elif numero > maximo:
        return f"maximo {maximo}"
    else:
        return f"recortado {numero}"

num1=int(random.randint(1,200))
num2=int(random.randint(1,50))
num3=int(random.randint(51,100))

print(f"a recortar: {num1}, minimo {num2}, maximo {num3}")

numero_recortado = recortar(num1, num2, num3)

print(numero_recortado)  
