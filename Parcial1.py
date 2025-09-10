libros = [{"idlibro" : "1", "nombre" : "Cien años de soledad", "autor" : "Gabriel García Márquez", "categoria" : "Novela", "año" : "1967", "stock" : "7"},
          {"idlibro" : "2", "nombre" : "El amor en los tiempos del cólera", "autor" : "Gabriel García Márquez", "categoria" : "Novela", "año" : "1985", "stock" : "5"},
          {"idlibro" : "3", "nombre" : "La hojarasca", "autor" : "Gabriel García Márquez", "categoria" : "Novela", "año" : "1955", "stock" : "4"},
          {"idlibro" : "4", "nombre" : "Rayuela", "autor" : "Julio Cortazar", "categoria" : "Novela", "año" : "1963", "stock" : "6"},
          {"idlibro" : "5", "nombre" : "Pedro Páramo", "autor" : "Juan Rulfo", "categoria" : "Novela", "año" : "1955", "stock" : "3"},
          {"idlibro" : "6", "nombre" : "El origen de las especies", "autor" : "Charles Darwin", "categoria" : "Ciencia", "año" : "1859", "stock" : "2"},
          {"idlibro" : "7", "nombre" : "Una breve historia del tiempo", "autor" : "Stephen Hawking", "categoria" : "Ciencia", "año" : "1988", "stock" : "4"},
          {"idlibro" : "8", "nombre" : "Introducción a la Filosofía", "autor" : "José Ferrater Mora", "categoria" : "Filosofia", "año" : "1960", "stock" : "5"},
          {"idlibro" : "9", "nombre" : "Crítica de la razón pura", "autor" : "Immanuel Kant", "categoria" : "Filosofia", "año" : "1781", "stock" : "1"},
          {"idlibro" : "10", "nombre" : "El arte de la guerra", "autor" : "Sun Tzu", "categoria" : "Estrategia", "año" : "500", "stock" : "6"}]

usuarios =[{"idusuario" : "1", "nombre" : "Ana", "email" : "ana@email.com"},
           {"idusuario" : "2", "nombre" : "Carlos", "email" : "carlos@email.com"},
           {"idusuario" : "3", "nombre" : "Laura", "email" : "laura@email.com"}]

prestamos =[{"id" : "1", "idusuario" : "1", "idlibro" : "2", "cantidad" : "1", "fecha" : "2024-03-01"},
            {"id" : "2", "idusuario" : "2", "idlibro" : "1", "cantidad" : "2", "fecha" : "2024-03-02"},
            {"id" : "3", "idusuario" : "2", "idlibro" : "2", "cantidad" : "1", "fecha" : "2024-03-10"}]

class F:
    def write(self, filename, dictionary):
        enable = 1
        with open(filename, "w", encoding="utf-8") as f:
            labels = list(dictionary[0].keys())
            for label in labels:
                f.write(label + ",")
            f.write("activo" + "\n")
            for a in dictionary:
                for d in a.values():
                    f.write(d )
                    f.write(",")
                f.write(str(enable)+"\n")
    
    def read(self, filename):
        try:
            with open(filename, "r", encoding = "utf-8") as f:
                for linea in f:
                    print(linea.strip())
        except FileNotFoundError:
            print ("El archivo no existe")
    
    def ordenarlibrosaños(self, libros):
        n = len(libros)
        for i in range (n):
            for j in range(0, n - i - 1):
                libro_1 = float(libros[j]["año"])
                libro_2 = float(libros[j + 1]["año"])
                if libro_1 > libro_2:
                    libros[j], libros[j + 1] = libros[j + 1], libros[j]
        print("Libros ordenados en años de menor a mayor:")
        for l in libros:
            print(f"id = {l['idlibro']}, autor = {l['autor']}, año = {l['año']}, stock = {l['stock']}" )

    def nuevousuario(self, usuario):
        nuevo_id = str(len(usuario) + 1)
        nombre = input("Ingrese el nombre del usuario: ")
        email = input("Ingrese el email del usuario: ")
        usuario = {"idusuario" : nuevo_id, "nombre" : nombre, "email" : email}
        usuarios.append(usuario)
        print("Usuario agregado con id: " + nuevo_id)

    def calcularprestamoslibro():
        for l in libros:
            t = 0
            idlibro = l["idlibro"]
            nombre = l["nombre"]
            for p in prestamos:
                if p["idlibro"] == idlibro:
                    t =+ int(p["cantidad"])
                    print(f"id = {l['idlibro']}, nombre = {l['nombre']}, prestamos = {t} ")
                    break
        total_prestamos = [{"idlibro" : 1, "nombre" : "Cien años de soledad", "prestamos" : "t"},
                           {"idlibro" : 2, "nombre" : "El amor en los tiempos del cólera", "prestamos" : "t"}]
        f.write("total_prestamos.csv", total_prestamos)
        

    def prestamosusuarios():
        for u in usuarios:
            idusuario = u["idusuario"]
            nombre = u["nombre"]
            email = u["email"]
            for p in prestamos:
                if p["idusuario"] == idusuario:
                    print(f"nombre = {u['nombre']}, email = {u['email']}, id = {["idusuario"]}")



f = F()
f.write("libros.csv", libros)
f.write("usuarios.csv", usuarios)
f.write("prestamos.csv", prestamos)

while True:
    print("1. Ver libros ordenados por año de publicación (ascendente)")
    print("2. Agregar un nuevo usuario.")
    print("3. Calcular total de préstamos por libro")
    print("4. Ver usuarios que han realizado préstamos")
    print("5. Salir")
    print("Seleccione una opción: ")
    op = input()
    if op == "1":
        F.ordenarlibrosaños("libros.csv", libros)
    if op == "2":
        F.nuevousuario("usuarios.csv", usuarios)
        f.write("usuarios.csv", usuarios)
    if op == "3":
        F.prestamosusuarios()
    if op == "4":
        F.calcularprestamoslibro()
    if op == "5":
        break
