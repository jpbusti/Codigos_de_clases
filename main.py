# Archivo principal
with open("archivo_secuencial.txt", "w") as file:
    file.write("0|Juan, 30 años\n")
    file.write("1|María, 25 años\n")
    file.write("2|Pedro, 40 años\n")

# Crear índice
indice = {}
with open("archivo_secuencial.txt", "r") as file:
    for line in file:
        pos, data = line.split("|")
        clave = data.split(",")[0]  # Nombre como clave
        indice[clave.strip()] = int(pos)

# Búsqueda usando índice
busqueda = "María"
if busqueda in indice:
    with open("archivo_secuencial.txt", "r") as file:
        file.seek(indice[busqueda] * 15)  # Asumiendo longitud fija
        print(file.readline())
else:
    print(f"{busqueda} no encontrado.")