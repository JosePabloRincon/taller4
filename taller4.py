import sqlite3

# Conexión a la base de datos
def connect_db():
    conn = sqlite3.connect('usuarios.db')
    return conn

# Crear la tabla de usuarios
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            telefono TEXT NOT NULL,
            email TEXT NOT NULL,
            ciudad TEXT NOT NULL,
            direccion TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()