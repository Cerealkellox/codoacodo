cesta={}

def aplicar_descuento(monto,descuento):
    desc=monto*descuento/100
    total=monto-desc
    return(total)

def aplicar_iva(monto,iva):
    iva2=monto*iva/100
    total=monto+iva2
    return(total)

def agregar_producto(producto,valor):
    cesta[producto]=valor   


n=True
total=int(0)

while n==True:

    print('''
    -------------------------------------------
    ##### favor de elegir opcion #####
    1- agregar producto a la cesta con escuento
    2- agregar producto a la cesta con iva
    3- agregar producto normal
    0- finalizar y mostrar total
    -------------------------------------------
    ''')

    seleccion=int(input("ingrese opcion: "))

    if seleccion==0: #salir
        n=False

    elif seleccion==1: #conn descuennto
        
        producto_venta=str(input("ingrese nombre de producto: "))
        precio_venta=float(input("ingrese el valor del producto: "))
        descuento_venta=int(input("ingrese porcentaje de desuento: "))
        venta=aplicar_descuento(precio_venta,descuento_venta)
        total=total+venta
        cesta[producto_venta]=venta

    elif seleccion==2: #con iva
        
        producto_venta=str(input("ingrese nombre de producto: "))
        precio_venta=float(input("ingrese el valor del producto: "))
        valor_iva=int(21)
        venta=aplicar_iva(precio_venta,valor_iva)
        total=total+venta
        cesta[producto_venta]=venta
        
    elif seleccion==3: #normal
        
        producto_venta=str(input("ingrese nombre de producto: "))
        precio_venta=float(input("ingrese el valor del producto: "))
        venta=precio_venta
        total=total+venta
        cesta[producto_venta]=precio_venta

    else: #error opcion ingresada
        
        print("debe elegir 0,1,2,3")

print("------------------------------")
for producto, valor in cesta.items():
    print(f"{producto} : ${valor:.2f}")
print("------------------------------")  
print(f"total a pagar: ${total:.2f}")
print("------------------------------")

#print(cesta)