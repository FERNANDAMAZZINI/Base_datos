import sqlite3

# Conectar (o crear) la base de datos
conn = sqlite3.connect('libreria.db')

# Crear un cursor
cursor = conn.cursor()

# Crear tablas
cursor.execute('''
CREATE TABLE IF NOT EXISTS autores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    nacionalidad TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS libros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor_id INTEGER,
    anio_publicacion INTEGER,
    FOREIGN KEY (autor_id) REFERENCES autores(id)
)
''')

# Insertar datos ficticios en autores
autores = [
    ("Gabriel García Márquez", 'Colombiana'),
    ('Jane Austen', 'Británica'),
    ('Fiódor Dostoyevski', 'Rusa'),
    ('Haruki Murakami', 'Japonesa'),
]

cursor.executemany('''
INSERT INTO autores (nombre, nacionalidad) VALUES (?, ?)
''', autores)

# Insertar datos ficticios en libros
libros = [
    ('Cien años de soledad', 1, 1967),
    ('Orgullo y prejuicio', 2, 1813),
    ('Crimen y castigo', 3, 1866),
    ('Kafka en la orilla', 4, 2002),
]

cursor.executemany('''
INSERT INTO libros (titulo, autor_id, anio_publicacion) VALUES (?, ?, ?)
''', libros)

# Guardar (commit) los cambios
conn.commit()

# Consultar datos de autores
print("Autores:")
cursor.execute('SELECT * FROM autores')
for fila in cursor.fetchall():
    print(fila)

# Consultar datos de libros
print("\nLibros:")
cursor.execute('SELECT * FROM libros')
for fila in cursor.fetchall():
    print(fila)

# Cerrar la conexión
conn.close()
