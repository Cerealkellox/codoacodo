#pedir dos nombres, y chequear si cionciden primera y ultima letra

nombreUno=str(input("ingrese primer nombre: >>>"))
nombreDos=str(input("ingrese segundo nombre: >>>"))

#codigo string-methods obtenido de https://docs.python.org/es/3/library/stdtypes.html#string-methods
#obtengo las primera letra de los nombres
primeraLetra1=nombreUno[0]
primeraLetra2=nombreDos[0]

#obtengo la ultima lesta de los nombres
ultimaLetra1=nombreUno[-1]
ultimaLetra2=nombreDos[-1]

#hago las comparaciones
if primeraLetra1==primeraLetra2 and ultimaLetra1==ultimaLetra2:
    print("hay coincidencia")
else:
    print("no hay coincidencia")
