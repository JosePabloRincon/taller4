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

# Función para agregar un nuevo usuario
def create_user(nombre, telefono, email, ciudad, direccion):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO usuarios (nombre, telefono, email, ciudad, direccion)
        VALUES (?, ?, ?, ?, ?)
    ''', (nombre, telefono, email, ciudad, direccion))
    conn.commit()
    conn.close()

# Función para leer todos los usuarios
def read_users():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios')
    users = cursor.fetchall()
    conn.close()
    return users

# Función para actualizar el teléfono de un usuario
def update_phone(user_id, new_phone):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE usuarios SET telefono = ? WHERE id = ?
    ''', (new_phone, user_id))
    conn.commit()
    conn.close()

# Función para actualizar el email de un usuario
def update_email(user_id, new_email):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE usuarios SET email = ? WHERE id = ?
    ''', (new_email, user_id))
    conn.commit()
    conn.close()

# Función para actualizar todos los datos de un usuario
def update_user(user_id, new_telefono, new_email, new_ciudad, new_direccion):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE usuarios SET telefono = ?, email = ?, ciudad = ?, direccion = ? WHERE id = ?
    ''', (new_telefono, new_email, new_ciudad, new_direccion, user_id))
    conn.commit()
    conn.close()

# Función para borrar un usuario
def delete_user(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM usuarios WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()  