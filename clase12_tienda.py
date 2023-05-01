'''
- Una tienda de ropa tiene 4 planes según como se decida efectuar el pago:
Plan 1: pago en efectivo, 15% de descuento del precio publicado.
Plan 2: Un solo pago por plataformas digitales, se realiza un 5% del precio publicado.
Plan 3: 3 cuotas sin interés, paga el precio publicado en 3 partes.
Plan 4: 12 cuotas, al precio publicado se le agregara el 20% y se pagaran 12 cuotas iguales de este nuevo valor.

El cliente (la tienda) nos pide que al ingresar por sistema el valor del precio publicado, nos regrese una pantalla con el detalle y los valores de los distintos planes.

Una posible resolucion en PSeInt

  Definir  precio, plan1, plan2, plan3, plan4 Como Real
	Escribir "precio de la prenda"
	Leer precio
	plan1 = precio * 0.85
	plan2 = precio * 0.95
	plan3 = precio / 3
	plan4 = (precio * 1.20)/12
	Escribir "los planes de pago son: "
	Escribir "Plan1 efectivo 15% de descuento $", plan1
	Escribir "plan2 plataforma digital 5% de descuento $", plan2
	Escribir "plan3 tres cuotas sin interes de: $", plan3
	Escribir "plan4 20% de interes en 12 cuotas de: $", plan4
'''
precio=float(input("ingrese el precio de la venta $"))


print ("################ plan de pago ################")
print ('''
1 - plan 1: efecticvo 15% de descuento
2 - plan 2: plataforma digital 5% de descuento
3 - plan 3: tres cuotas sin interes
4 - plan 4: 12 cuotas con 20% de interes
''')

opcion=str(input("ingrese opcion de pago: "))
print("=========================")
if opcion=="1":
    print("    pago en efectivo")
    print("=========================")
    print(f"valor a pagar {precio}")
    descuento=precio*0.15
    print(f"descuento 15% {descuento:0.2f}")
    aPagar=precio-descuento
    print(f"total a pagar {aPagar:0.2f}")
elif opcion=="2":
    print(" pago plataforma digital")
    print("=========================")
    print(f"valor a pagar {precio}")
    descuento=precio*0.05
    print(f"descuento 5% {descuento:0.2f}")
    aPagar=precio-descuento
    print(f"total a pagar {aPagar:0.2f}")
    print("=========================")
elif opcion=="3":
    print("   plan 3 cuotas fijas")
    print("=========================")
    print(f"valor a pagar {precio}")
    cuota=precio/3
    print(f"3 cuotas de {cuota:0.2f}")
    aPagar=cuota * 3
    print(f"total a pagar {aPagar:0.2f}")
elif opcion=="4":
    print("   plan 4 seleccionado")
    print("=========================")
    print(f"valor a pagar {precio}")
    interes=precio*0.12
    aPagar=precio+interes
    cuota=aPagar/12
    print(f"12 cuotas de ${cuota:0.2f}")
    print(f"total a pagar {aPagar:0.2f}")
else:
    print("debe seleccionar una opcion de pago valida")
    
print("=========================")