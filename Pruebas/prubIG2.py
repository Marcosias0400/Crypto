import tkinter as tk

def accion_boton1():
    print("Botón 1 presionado")

def accion_boton2():
    print("Botón 2 presionado")

def accion_boton3():
    print("Botón 3 presionado")

def accion_boton4():
    print("Botón 4 presionado")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ventana con botones y entradas de texto")
ventana.geometry("400x300")

# Configurar las columnas y filas para que se expandan de forma proporcional
for i in range(4):
    ventana.columnconfigure(i, weight=1)
    ventana.rowconfigure(i, weight=1)

# Crear las entradas de texto
entrada1 = tk.Entry(ventana)
entrada2 = tk.Entry(ventana)
entrada3 = tk.Entry(ventana)
entrada4 = tk.Entry(ventana)

# Crear los botones
boton1 = tk.Button(ventana, text="Botón 1", command=accion_boton1)
boton2 = tk.Button(ventana, text="Botón 2", command=accion_boton2)
boton3 = tk.Button(ventana, text="Botón 3", command=accion_boton3)
boton4 = tk.Button(ventana, text="Botón 4", command=accion_boton4)

# Colocar las entradas de texto en la ventana
entrada1.grid(row=0, column=0, padx=10, pady=10)
entrada2.grid(row=1, column=0, padx=10, pady=10)
entrada3.grid(row=2, column=0, padx=10, pady=10)
entrada4.grid(row=3, column=0, padx=10, pady=10)

# Colocar los botones en la ventana
boton1.grid(row=0, column=1, padx=10, pady=10)
boton2.grid(row=1, column=1, padx=10, pady=10)
boton3.grid(row=2, column=1, padx=10, pady=10)
boton4.grid(row=3, column=1, padx=10, pady=10)

# Ejecutar el bucle principal
ventana.mainloop()

