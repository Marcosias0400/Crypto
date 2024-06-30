import tkinter as tk
from tkinter import messagebox

def verificar_acceso():
    usuario = entrada_usuario.get()
    contrasena = entrada_contrasena.get()
    
    # Aquí puedes añadir la lógica para verificar el usuario y la contraseña.
    # Por ejemplo, podrías comparar con valores predefinidos o consultar una base de datos.
    if usuario == "admin" and contrasena == "1234":
        messagebox.showinfo("Acceso Concedido", "¡Bienvenido!")
    else:
        messagebox.showerror("Acceso Denegado", "Usuario o contraseña incorrectos.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ventana de Acceso")
ventana.geometry("300x200")

# Crear las etiquetas y campos de entrada
label_usuario = tk.Label(ventana, text="Usuario")
label_usuario.pack(pady=5)

entrada_usuario = tk.Entry(ventana)
entrada_usuario.pack(pady=5)

label_contrasena = tk.Label(ventana, text="Contraseña")
label_contrasena.pack(pady=5)

entrada_contrasena = tk.Entry(ventana, show="*")
entrada_contrasena.pack(pady=5)

# Crear el botón de acceso
boton_acceso = tk.Button(ventana, text="Acceder", command=verificar_acceso)
boton_acceso.pack(pady=20)

# Ejecutar el bucle principal
ventana.mainloop()

