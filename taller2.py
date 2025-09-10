from pathlib import Path
while True:
    print("1. Crear archivo Datos.csv")
    print("2. Consultar saldo por nombre")
    print("3. Mostrar clientes con saldo mayor a 50")
    print("4. Salir")
    op = input("Seleccione una opción: ")
    if op == "1":
        Path("salida").mkdir(exist_ok=True)
        with open("salida/Datos.csv", "w", encoding="utf-8") as f:
            f.write("Cedula,Nombre,Saldo\n")
            f.write("12345,Jose,50.43\n")
            f.write("54321,Dario,43.12\n")
        print("Archivo Datos.csv creado correctamente.")
    elif op == "2":
        nombre = input("Ingrese el nombre a consultar: ")
        with open("salida/Datos.csv", "r", encoding="utf-8") as f:
            next(f)
            encontrado = False
            for linea in f:
                cedula, nombre_, saldo = linea.strip().split(",")
                if nombre == nombre_:
                    print(f"El saldo del cliente es de: {saldo}")
                    encontrado = True
                if not encontrado:
                    print("Cliente no encontrado.")
    elif op == "3":
        with open("salida/Datos.csv", "r", encoding="utf-8") as f:
            next(f)
            encontrado = False
            for linea in f:
                cedula, nombre_, saldo = linea.strip().split(",")
                if saldo > 50:
                    print(f"El cliente {nombre_} tiene un saldo mayor a 50")
                    encontrado = True
            if not encontrado:
                print("No hay clientes con saldo mayor a 50")
    elif op == "4":
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")