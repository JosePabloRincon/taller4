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

def menu():
    while True:
        print("\nMenú:")
        print("1. Crear usuario")
        print("2. Leer usuarios")
        print("3. Actualizar teléfono")
        print("4. Actualizar email")
        print("5. Actualizar todos los datos")
        print("6. Borrar usuario")
        print("7. Salir")
        
        choice = input("Seleccione una opción: ")
        
        if choice == '1':
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            ciudad = input("Ciudad: ")
            direccion = input("Dirección: ")
            create_user(nombre, telefono, email, ciudad, direccion)
        
        elif choice == '2':
            users = read_users()
            for user in users:
                print(user)
        
        elif choice == '3':
            user_id = int(input("ID del usuario a actualizar: "))
            new_phone = input("Nuevo teléfono: ")
            update_phone(user_id, new_phone)
        
        elif choice == '4':
            user_id = int(input("ID del usuario a actualizar: "))
            new_email = input("Nuevo email: ")
            update_email(user_id, new_email)
        
        elif choice == '5':
            user_id = int(input("ID del usuario a actualizar: "))
            new_telefono = input("Nuevo teléfono: ")
            new_email = input("Nuevo email: ")
            new_ciudad = input("Nueva ciudad: ")
            new_direccion = input("Nueva dirección: ")
            update_user(user_id, new_telefono, new_email, new_ciudad, new_direccion)
        
        elif choice == '6':
            user_id = int(input("ID del usuario a borrar: "))
            delete_user(user_id)
        
        elif choice == '7':
            break
        
        else:
                        print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    create_table()  # Crear la tabla al iniciar el programa
    # Agregar usuarios iniciales
    initial_users = [
        ("Juan Pérez", "123456789", "juan@example.com", "Madrid", "Calle Falsa 123"),
        ("Ana Gómez", "987654321", "ana@example.com", "Barcelona", "Avenida Siempre Viva 742"),
        ("Luis Martínez", "456789123", "luis@example.com", "Valencia", "Calle del Sol 456"),
        ("María López", "321654987", "maria@example.com", "Sevilla", "Plaza Mayor 789"),
        ("Carlos Ruiz", "654321789", "carlos@example.com", "Bilbao", "Calle del Mar 321"),
        ("Laura Fernández", "789123456", "laura@example.com", "Zaragoza", "Calle de la Luna 654"),
    ]

    for user in initial_users:
        create_user(*user)

    menu()  