import json

clientes = [{"id_cliente" : "1", "nombre" : "Juan", "apellido" : "Perez", "telefono" : "3123456789", "activo": 1},
            {"id_cliente" : "2", "nombre" : "Maria", "apellido" : "Gomez", "telefono" : "3123456786", "activo": 1},
            {"id_cliente" : "3", "nombre" : "Carlos", "apellido" : "Ramirez", "telefono" : "3123456787", "activo": 1}]

productos = [{"id_producto": "1", "nombre": "Laptop", "precio": "2500.00"},
             {"id_producto": "2", "nombre": "Mouse", "precio": "20.50"},
             {"id_producto": "3", "nombre": "Teclado", "precio": "45.00"},
             {"id_producto": "4", "nombre": "Monitor", "precio": "150.00"}]

ventas = [{"id_venta": "1", "id_cliente": "1", "id_producto": "1", "cantidad": "1"},
          {"id_venta": "2","id_cliente": "2", "id_producto": "2", "cantidad": "2"},
          {"id_venta": "3","id_cliente": "1","id_producto": "3","cantidad": "1"},
          {"id_venta": "4","id_cliente": "3","id_producto": "4","cantidad": "1"}]

class F:
    def write_json(self, filename, data):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def read_json(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def registrar_cliente(self, clientes_list):
        nuevo_id = str(len(clientes_list) + 1)
        nombre = input("Ingrese el nombre del cliente: ")
        apellido = input("Ingrese el apellido del cliente: ")
        telefono = input("Ingrese el telefono del cliente: ")
        cliente = {"id_cliente" : nuevo_id, "nombre" : nombre, "apellido" : apellido, "telefono" : telefono, "activo": 1}
        clientes_list.append(cliente)
        print("Cliente registrado con éxito.")
        return clientes_list
    
    def listar_clientes(self, clientes_list):
        print("\n--- Clientes Activos ---")
        for cliente in clientes_list:
            if cliente.get("activo", 1) == 1: # Filtra por clientes activos
                print(f"ID: {cliente['id_cliente']}, Nombre: {cliente['nombre']} {cliente['apellido']}, Teléfono: {cliente['telefono']}")

    def eliminar_cliente_logico(self, clientes_list, id_cliente):
        encontrado = False
        for cliente in clientes_list:
            if cliente['id_cliente'] == id_cliente:
                cliente["activo"] = 0
                encontrado = True
                print(f"Cliente con ID {id_cliente} ha sido inactivado lógicamente.")
                break
        if not encontrado:
            print("Cliente no encontrado.")
        return clientes_list

    def registrar_producto(self, productos_list):
        nuevo_id = str(len(productos_list) + 1)
        nombre = input("Ingrese el nombre del producto: ")
        precio = input("Ingrese el precio del producto: ")
        producto = {"id_producto" : nuevo_id, "nombre" : nombre, "precio": precio}
        productos_list.append(producto)
        print("Producto registrado con éxito.")
        return productos_list

    def registrar_venta(self, ventas_list):
        nuevo_id = str(len(ventas_list) + 1)
        id_cliente = input("Ingrese el id del cliente: ")
        id_producto = input("Ingrese el id del producto: ")
        cantidad = input("Ingrese la cantidad del producto: ")
        venta = {"id_venta" : nuevo_id, "id_cliente" : id_cliente, "id_producto" : id_producto, "cantidad" : cantidad}
        ventas_list.append(venta)
        print("Venta registrada con éxito.")
        return ventas_list

    def listar_ventas_cliente(self, clientes_list, productos_list, ventas_list):
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        cliente_encontrado = None
        for c in clientes_list:
            if c["nombre"].lower() == nombre_cliente.lower():
                cliente_encontrado = c
                break
        
        if not cliente_encontrado:
            print("Cliente no encontrado.")
            return

        id_cliente = cliente_encontrado["id_cliente"]
        total_gasto = 0
        print(f"\n--- Ventas de {cliente_encontrado['nombre']} {cliente_encontrado['apellido']} ---")
        for v in ventas_list:
            if v["id_cliente"] == id_cliente:
                id_producto = v["id_producto"]
                cantidad = int(v["cantidad"])
                
                for p in productos_list:
                    if p["id_producto"] == id_producto:
                        precio = float(p["precio"])
                        subtotal = precio * cantidad
                        total_gasto += subtotal
                        print(f"Producto: {p['nombre']}, Cantidad: {cantidad}, Subtotal: ${subtotal:.2f}")
                        break
        print(f"\nTotal gastado por el cliente: ${total_gasto:.2f}")

    def ordenar_productos_por_precio(self, productos_list):
        productos_ordenados = sorted(productos_list, key=lambda p: float(p['precio']), reverse=True)
        print("\n--- Productos ordenados por precio (mayor a menor) ---")
        for producto in productos_ordenados:
            print(f"ID: {producto['id_producto']}, Nombre: {producto['nombre']}, Precio: ${float(producto['precio']):.2f}")

# Instanciar la clase F
f = F()

# Iniciar con la data inicial, añadiendo el estado "activo"
for c in clientes:
    c["activo"] = 1
f.write_json("clientes.json", clientes)
f.write_json("productos.json", productos)
f.write_json("ventas.json", ventas)

while True:
    print("\n--- Menú de Gestión ---")
    print("1. Registrar un cliente")
    print("2. Listar clientes (activos)")
    print("3. Eliminar (inactivar) un cliente")
    print("4. Registrar un producto")
    print("5. Guardar una venta")
    print("6. Listar las ventas realizadas por cliente")
    print("7. Ordenar productos por precio")
    print("8. Salir")
    
    op = input("Seleccione una opción: ")

    if op == "1":
        clientes_data = f.read_json("clientes.json")
        clientes_data = f.registrar_cliente(clientes_data)
        f.write_json("clientes.json", clientes_data)
    elif op == "2":
        clientes_data = f.read_json("clientes.json")
        f.listar_clientes(clientes_data)
    elif op == "3":
        id_cliente_eliminar = input("Ingrese el ID del cliente a eliminar (inactivar): ")
        clientes_data = f.read_json("clientes.json")
        clientes_data = f.eliminar_cliente_logico(clientes_data, id_cliente_eliminar)
        f.write_json("clientes.json", clientes_data)
    elif op == "4":
        productos_data = f.read_json("productos.json")
        productos_data = f.registrar_producto(productos_data)
        f.write_json("productos.json", productos_data)
    elif op == "5":
        ventas_data = f.read_json("ventas.json")
        ventas_data = f.registrar_venta(ventas_data)
        f.write_json("ventas.json", ventas_data)
    elif op == "6":
        clientes_data = f.read_json("clientes.json")
        productos_data = f.read_json("productos.json")
        ventas_data = f.read_json("ventas.json")
        f.listar_ventas_cliente(clientes_data, productos_data, ventas_data)
    elif op == "7":
        productos_data = f.read_json("productos.json")
        f.ordenar_productos_por_precio(productos_data)
    elif op == "8":
        print("¡Adiós!")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")