from math import *
from random import randint, random, uniform

entero = 986
real = 45.9887878

#redondeo: round(x)
# puedo indicarle cantidad de dígitos: round(x, 2)
print(round(234.367884))

# valor absoluto: abs()
print(abs(-43.4))

# Numeros aleatorios, se necesita importar libreria random
print(randint(1, 5)) # retorna un número entero entre 1 y 5 inclusive
print(random()) # retorna un aleatorio en el rango 0.0 <= X < 1.0
print(uniform(4.3, 5.8)) # retorna un número decimal dentro de los límites



# Necesitamos importar el modulo math
# from math import *
# Info completa: https://docs.python.org/es/3/library/stdtypes.html#string-methods


# Truncado(parte entera): trunc(x)
print(trunc(234.45))


# Potencia: pow(x,y)
print(pow(5,3))

# Raiz cuadrada: sqrt(x)
print(sqrt(100))