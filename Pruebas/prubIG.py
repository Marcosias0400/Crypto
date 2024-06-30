import tkinter as tk

def accion_boton1():
    print("Botón 1 presionado")

def accion_boton2():
    print("Botón 2 presionado")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ventana con dos botones")
ventana.geometry("300x200")

# Crear los botones
boton1 = tk.Button(ventana, text="Botón 1", command=accion_boton1)
boton2 = tk.Button(ventana, text="Botón 2", command=accion_boton2)

# Colocar los botones en la ventana
boton1.pack(pady=10)
boton2.pack(pady=10)

# Ejecutar el bucle principal
ventana.mainloop()

