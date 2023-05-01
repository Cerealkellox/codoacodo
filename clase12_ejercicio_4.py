#pediremos al usuario que ingrese un dia de la semana, segun el dia, daremos un mensaje

diasemana=str(input("Favor de ingresar un dia de la semana "))

#dar msg si es: lunes, viernes, sab o dom, resto dias
print("♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦")
if diasemana=="lunes":
    print("como adoro comenzar la semana laboral")
elif diasemana=="viernes":
    print("como adoro cuando la semana termina normal")
elif diasemana=="viernes" or diasemana=="domingo":
    print("los fines de semana se aprovehc a limpiar y lavar")
else:
    print("dia normal de la semana")
print("♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦")