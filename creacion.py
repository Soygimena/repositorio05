import sqlite3

def crear_base_datos():
    conn = sqlite3.connect('instituto.db')  # Crea el archivo de base de datos
    cursor = conn.cursor()

    # Crear tabla de estudiantes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS estudiantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            fecha_nacimiento DATE NOT NULL,
            direccion TEXT,
            telefono TEXT
        )
    ''')

    # Crear tabla de matrículas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS matriculas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            estudiante_id INTEGER,
            fecha_matricula DATE NOT NULL,
            grado TEXT NOT NULL,
            FOREIGN KEY(estudiante_id) REFERENCES estudiantes(id)
        )
    ''')

    # Crear tabla de pagos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pagos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            estudiante_id INTEGER,
            tipo_pago TEXT NOT NULL,
            cantidad REAL NOT NULL,
            fecha_pago DATE NOT NULL,
            FOREIGN KEY(estudiante_id) REFERENCES estudiantes(id)
        )
    ''')

    conn.commit()
    conn.close()

# Ejecutamos la función para crear la base de datos
crear_base_datos()
