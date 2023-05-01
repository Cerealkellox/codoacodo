#importamos libreria
from math import *
from random import randint, random, uniform

#pedimos al usuario que ingrese un numero, si es el numero 1000, gana

numeroUser=str(input("ingrese un numero del 1 al 9999 --> :"))
numeroGanador=str(randint(0,9999))
print(f"numero aleatorio {numeroGanador}")
if numeroUser==numeroGanador:
    print("has ganado el premio")
else: 
    print("sigue ppartidipando")
