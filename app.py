import tkinter as tk
from tkinter import messagebox
import sqlite3

# Función para conectar a la base de datos
def conectar_db():
    return sqlite3.connect('instituto.db')

# Función para registrar un estudiante y agregarlo a una lista
def registrar_estudiante():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    fecha_nacimiento = entry_fecha_nacimiento.get()
    direccion = entry_direccion.get()
    telefono = entry_telefono.get()

    if nombre and apellido and fecha_nacimiento:
        # Conectar a la base de datos y registrar el estudiante
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute(''' 
            INSERT INTO estudiantes (nombre, apellido, fecha_nacimiento, direccion, telefono)
            VALUES (?, ?, ?, ?, ?)
        ''', (nombre, apellido, fecha_nacimiento, direccion, telefono))
        conn.commit()
        conn.close()

        # Agregar el estudiante a la lista de estudiantes
        estudiantes.append({'nombre': nombre, 'apellido': apellido, 'fecha_nacimiento': fecha_nacimiento, 'direccion': direccion, 'telefono': telefono})

        # Mostrar mensaje de éxito
        messagebox.showinfo('Éxito', 'Estudiante registrado con éxito')
        actualizar_lista()
    else:
        messagebox.showerror('Error', 'Por favor ingrese todos los datos obligatorios')

# Función para actualizar la lista de estudiantes en la interfaz
def actualizar_lista():
    # Limpiar la lista de estudiantes mostrada
    listbox_estudiantes.delete(0, tk.END)
    
    # Agregar los estudiantes a la lista
    for estudiante in estudiantes:
        listbox_estudiantes.insert(tk.END, f"{estudiante['nombre']} {estudiante['apellido']} - {estudiante['fecha_nacimiento']}")

# Lista para almacenar estudiantes en memoria
estudiantes = []

# Función para mostrar el botón de retroceso
def crear_boton_retroceder(func):
    return tk.Button(root, text="Retroceder", font=button_font, bg="#FF6347", fg="white", command=func)

# Pantalla de Inicio de Sesión
def mostrar_inicio_sesion():
    # Ocultar la pantalla de bienvenida
    label_bienvenida.grid_forget()
    btn_entrar.grid_forget()
    label_viviate.grid_forget()  # Eliminar "VIVIATE" al mostrar el login

    # Mostrar la pantalla de login
    label_usuario.grid(row=0, column=0, padx=10, pady=10)
    entry_usuario.grid(row=0, column=1, padx=10, pady=10)
    
    label_contraseña.grid(row=1, column=0, padx=10, pady=10)
    entry_contraseña.grid(row=1, column=1, padx=10, pady=10)

    btn_login.grid(row=2, column=0, columnspan=2, pady=20)

    # Agregar botones adicionales
    btn_salir = tk.Button(root, text="Salir", font=button_font, bg="#FF6347", fg="white", command=root.quit)
    btn_salir.grid(row=3, column=0, columnspan=2, pady=10)

    # Agregar el botón de retroceder
    btn_retroceder = crear_boton_retroceder(mostrar_bienvenida)
    btn_retroceder.grid(row=4, column=0, columnspan=2, pady=10)

# Función para verificar usuario y contraseña (aquí se puede conectar con una base de datos)
def verificar_login():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()

    # Aquí puedes agregar una verificación real del usuario y contraseña
    if usuario == "admin" and contraseña == "1234":
        mostrar_registro_estudiante()
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# Pantalla de Registro de Estudiantes
def mostrar_registro_estudiante():
    # Limpiar la ventana y mostrar el formulario de registro
    for widget in root.winfo_children():
        widget.grid_forget()

    # Mostrar los elementos de registro de estudiante
    label_nombre.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    entry_nombre.grid(row=0, column=1, padx=10, pady=10)
    
    label_apellido.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    entry_apellido.grid(row=1, column=1, padx=10, pady=10)
    
    label_fecha_nacimiento.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    entry_fecha_nacimiento.grid(row=2, column=1, padx=10, pady=10)

    label_direccion.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    entry_direccion.grid(row=3, column=1, padx=10, pady=10)
    
    label_telefono.grid(row=4, column=0, padx=10, pady=10, sticky="w")
    entry_telefono.grid(row=4, column=1, padx=10, pady=10)

    btn_registrar.grid(row=5, column=0, columnspan=2, padx=10, pady=20)

    label_lista.grid(row=6, column=0, columnspan=2, pady=10)
    listbox_estudiantes.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    # Botón para mostrar la lista de estudiantes
    btn_ver_estudiantes = tk.Button(root, text="Ver Estudiantes", font=button_font, bg="#4CAF50", fg="white", command=actualizar_lista)
    btn_ver_estudiantes.grid(row=8, column=0, columnspan=2, pady=10)

    # Agregar el botón de retroceder
    btn_retroceder = crear_boton_retroceder(mostrar_inicio_sesion)
    btn_retroceder.grid(row=9, column=0, columnspan=2, pady=10)

# Función para mostrar la pantalla de bienvenida
def mostrar_bienvenida():
    # Limpiar la ventana y mostrar la pantalla de bienvenida
    for widget in root.winfo_children():
        widget.grid_forget()

    label_bienvenida.grid(row=0, column=0, columnspan=2, padx=10, pady=50)

    btn_entrar.grid(row=1, column=0, columnspan=2, pady=20)

    label_viviate.grid(row=9, column=0, columnspan=2, pady=20)  # Coloca "VIVIATE" en la parte inferior, centrado

# Crear ventana principal
root = tk.Tk()
root.title('Gestión Administrativa Institucional')

# Configuración de la ventana
root.geometry('500x500')

# Establecer fondo con un color bonito, por ejemplo, un tono pastel
root.config(bg="#f0e0d6")  # Color de fondo pastel suave (puedes cambiar este valor por otros colores)

# Crear un estilo para las etiquetas, entradas y botones
label_font = ('Arial', 12)
entry_font = ('Arial', 12)
button_font = ('Arial', 12, 'bold')

# Pantalla de bienvenida (inicio)
label_bienvenida = tk.Label(root, text="INSTITUCIÓN EDUCATIVA SEÑOR CAUTIVO", font=('Arial', 18, 'bold'), bg="#f0e0d6")
label_bienvenida.grid(row=0, column=0, columnspan=2, padx=10, pady=50, sticky='nsew')

# Botón para entrar
btn_entrar = tk.Button(root, text="Entrar", font=button_font, bg="#4CAF50", fg="white", command=mostrar_inicio_sesion)
btn_entrar.grid(row=1, column=0, columnspan=2, pady=20, sticky='nsew')

# Etiqueta para el texto "VIVIATE" en la parte inferior (solo en la primera pantalla)
label_viviate = tk.Label(root, text="VIVIATE", font=('Arial', 16, 'italic', 'bold'), bg="#f0e0d6")
label_viviate.grid(row=9, column=0, columnspan=2, pady=20, sticky='nsew')  # Coloca "VIVIATE" en la parte inferior, centrado

# Pantalla de login (usuario y contraseña)
label_usuario = tk.Label(root, text="Usuario", font=label_font, bg="#f0e0d6")
entry_usuario = tk.Entry(root, font=entry_font)

label_contraseña = tk.Label(root, text="Contraseña", font=label_font, bg="#f0e0d6")
entry_contraseña = tk.Entry(root, font=entry_font, show="*")

btn_login = tk.Button(root, text="Iniciar sesión", font=button_font, bg="#4CAF50", fg="white", command=verificar_login)

# Pantalla de registro de estudiante
label_nombre = tk.Label(root, text="Nombre", font=label_font, bg="#f0e0d6")
entry_nombre = tk.Entry(root, font=entry_font)

label_apellido = tk.Label(root, text="Apellido", font=label_font, bg="#f0e0d6")
entry_apellido = tk.Entry(root, font=entry_font)

label_fecha_nacimiento = tk.Label(root, text="Fecha de Nacimiento (AAAA-MM-DD)", font=label_font, bg="#f0e0d6")
entry_fecha_nacimiento = tk.Entry(root, font=entry_font)

label_direccion = tk.Label(root, text="Dirección", font=label_font, bg="#f0e0d6")
entry_direccion = tk.Entry(root, font=entry_font)

label_telefono = tk.Label(root, text="Teléfono", font=label_font, bg="#f0e0d6")
entry_telefono = tk.Entry(root, font=entry_font)

# Botón para registrar estudiante
btn_registrar = tk.Button(root, text="Registrar Estudiante", font=button_font, bg="#4CAF50", fg="white", command=registrar_estudiante)

# Lista para mostrar los estudiantes registrados
label_lista = tk.Label(root, text="Lista de Estudiantes", font=label_font, bg="#f0e0d6")
listbox_estudiantes = tk.Listbox(root, font=('Arial', 10), width=40, height=10)

# Ejecutar la ventana principal
mostrar_bienvenida()
root.mainloop()
