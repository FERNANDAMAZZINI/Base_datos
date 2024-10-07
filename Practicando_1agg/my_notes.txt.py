
# Abrir el archivo en modo de escritura ('w') para agregar notas personales
with open('notas_personales.txt', 'w') as archivo:
    # Escribir notas en el archivo
    archivo.write("Nota 1: visitar a mama.\n")
    archivo.write("Nota 2: estudiar los sabados.\n")
    archivo.write("Nota 3: estudiar ingles.\n")

# Abrir el archivo en modo de lectura ('r') para leer las notas
with open('notas_personales.txt', 'r') as archivo:
    # Leer todas las líneas del archivo
    notas = archivo.readlines()
    # Imprimir cada nota en la consola
    for nota in notas:
        print(nota.strip())  # Usar strip() para eliminar saltos de línea
