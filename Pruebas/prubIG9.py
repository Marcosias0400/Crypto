import tkinter as tk
from tkinter import messagebox

def verificar_acceso():
    usuario = entrada_usuario.get()
    contrasena = entrada_contrasena.get()
    
    if usuario == "admin" and contrasena == "1234":
        messagebox.showinfo("Acceso Concedido", "¡Bienvenido!")
        abrir_ventana_principal()
    else:
        messagebox.showerror("Acceso Denegado", "Usuario o contraseña incorrectos.")

def abrir_ventana_principal():
    global ventana_principal
    ventana_acceso.withdraw()  # Ocultar la ventana de acceso en lugar de destruirla

    ventana_principal = tk.Toplevel()  # Crear una nueva ventana secundaria
    ventana_principal.title("Ventana Principal")
    ventana_principal.geometry("300x200")

    label_bienvenida = tk.Label(ventana_principal, text="¡Bienvenido a la ventana principal!")
    label_bienvenida.pack(pady=20)

    boton_cerrar = tk.Button(ventana_principal, text="Cerrar", command=ventana_principal.destroy)
    boton_cerrar.pack(pady=10)

    boton_retorno = tk.Button(ventana_principal, text="Volver", command=volver_a_ventana_acceso)
    boton_retorno.pack(pady=10)

def volver_a_ventana_acceso():
    ventana_principal.destroy()  # Cerrar la ventana principal
    ventana_acceso.deiconify()  # Mostrar la ventana de acceso nuevamente

# Crear la ventana de acceso
ventana_acceso = tk.Tk()
ventana_acceso.title("Ventana de Acceso")
ventana_acceso.geometry("300x200")

# Crear las etiquetas y campos de entrada
label_usuario = tk.Label(ventana_acceso, text="Usuario")
label_usuario.pack(pady=5)

entrada_usuario = tk.Entry(ventana_acceso)
entrada_usuario.pack(pady=5)

label_contrasena = tk.Label(ventana_acceso, text="Contraseña")
label_contrasena.pack(pady=5)

entrada_contrasena = tk.Entry(ventana_acceso, show="*")
entrada_contrasena.pack(pady=5)

# Crear el botón de acceso
boton_acceso = tk.Button(ventana_acceso, text="Acceder", command=verificar_acceso)
boton_acceso.pack(pady=20)

# Ejecutar el bucle principal
ventana_acceso.mainloop()

