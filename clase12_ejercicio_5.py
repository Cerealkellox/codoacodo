#segun numero, dar su valor absoluto
from math import *

numeroUser=float(input("ingresar un valor, positivo o negativo: "))

if numeroUser>0:
    print(trunc(numeroUser))
else:
    numeroUser=numeroUser*-1
    print(f"{numeroUser:0.0f}") 