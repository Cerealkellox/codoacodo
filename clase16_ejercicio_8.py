clientes={}

while True:
    print("Menú de opciones:")
    print("1. Añadir cliente")
    print("2. Eliminar cliente")
    print("3. Mostrar cliente")
    print("4. Listar todos los clientes")
    print("5. Listar clientes preferentes")
    print("6. Terminar")
    opcion = str(input("Selecciona una opción: "))
    print("-----------------------------")

    if opcion == "1":
        dni = input("Introduce el DNI del cliente: ")
        nombre = input("Introduce el nombre del cliente: ")
        direccion = input("Introduce la dirección del cliente: ")
        telefono = input("Introduce el teléfono del cliente: ")
        correo = input("Introduce el correo electrónico del cliente: ")
        preferente = input("¿Es un cliente preferente? (s/n): ").lower()
        if preferente == "s":
            preferente = True
        else:
            preferente = False
        # Creamos el diccionario con los datos del cliente y lo añadimos a la base de datos
        cliente = {"nombre": nombre, "direccion": direccion, "telefono": telefono, "correo": correo, "preferente": preferente}
        clientes[dni] = cliente
        print("Cliente añadido con éxito.")

    elif opcion == "2":
        dni = input("Introduce el DNI del cliente que deseas eliminar: ")
        if dni in clientes:
            del clientes[dni]
            print("Cliente eliminado con éxito.")
        else:
            print("El cliente no se encuentra en la base de datos.")

    elif opcion == "3":
        dni = input("Introduce el DNI del cliente que deseas mostrar: ")
        if dni in clientes:
            cliente = clientes[dni]
            print("-----------------------------")
            print("Datos del cliente:")
            print("Nombre:", cliente["nombre"])
            print("Dirección:", cliente["direccion"])
            print("Teléfono:", cliente["telefono"])
            print("Correo electrónico:", cliente["correo"])
            print("Preferente:", cliente["preferente"])
            print("-----------------------------")
        else:
            print("El cliente no se encuentra en la base de datos.")
    elif opcion == "4":
        print("Lista de clientes:")
        for dni, cliente in clientes.items():
            print(dni, "-", cliente["nombre"])
    elif opcion == "5":
            print("Lista de clientes preferentes:")
            for dni, cliente in clientes.items():
                if cliente["preferente"]:
                    print(dni, "-", cliente["nombre"])
    elif opcion == "6":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción del menú.")