import sqlite3

# Función para conectar a la base de datos
def conectar_db():
    return sqlite3.connect('guia_telefono.db')

# Función para crear la tabla
def crear_tabla():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS contactos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        telefono TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

# Función para agregar un contacto
def agregar_contacto(nombre, telefono):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO contactos (nombre, telefono) VALUES (?, ?)
    ''', (nombre, telefono))
    conn.commit()
    conn.close()

# Función para buscar un contacto
def buscar_contacto(nombre):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM contactos WHERE nombre LIKE ?
    ''', ('%' + nombre + '%',))
    resultados = cursor.fetchall()
    conn.close()
    return resultados

# Función para listar todos los contactos
def listar_contactos():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contactos')
    contactos = cursor.fetchall()
    conn.close()
    return contactos

# Función principal
def main():
    crear_tabla()

    while True:
        print("\nGuía de Teléfono")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Listar contactos")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            agregar_contacto(nombre, telefono)
            print("Contacto agregado.")

        elif opcion == '2':
            nombre = input("Nombre a buscar: ")
            resultados = buscar_contacto(nombre)
            if resultados:
                for contacto in resultados:
                    print(f"ID: {contacto[0]}, Nombre: {contacto[1]}, Teléfono: {contacto[2]}")
            else:
                print("No se encontraron contactos.")

        elif opcion == '3':
            contactos = listar_contactos()
            if contactos:
                for contacto in contactos:
                    print(f"ID: {contacto[0]}, Nombre: {contacto[1]}, Teléfono: {contacto[2]}")
            else:
                print("No hay contactos en la guía.")

        elif opcion == '4':
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == '__main__':
    main()
