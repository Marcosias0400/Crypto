import tkinter as tk

def mostrar_entrada(row):
    entrada = tk.Entry(ventana)
    entrada.grid(row=row, column=1, padx=10, pady=10)
    entradas.append(entrada)

    # Verificar si todas las entradas están creadas y mostrar el botón de ingresar texto
    if len(entradas) == 4:
        boton_ingresar_texto.grid(row=4, column=0, columnspan=2, pady=20)

def accion_boton1():
    print("Botón 1 presionado")
    mostrar_entrada(0)

def accion_boton2():
    print("Botón 2 presionado")
    mostrar_entrada(1)

def accion_boton3():
    print("Botón 3 presionado")
    mostrar_entrada(2)

def accion_boton4():
    print("Botón 4 presionado")
    mostrar_entrada(3)

def ingresar_texto():
    for i, entrada in enumerate(entradas):
        print(f"Entrada {i+1}: {entrada.get()}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ventana con botones y entradas de texto")
ventana.geometry("400x300")

# Crear una lista para almacenar las entradas de texto
entradas = []

# Crear los botones
boton1 = tk.Button(ventana, text="Botón 1", command=accion_boton1)
boton2 = tk.Button(ventana, text="Botón 2", command=accion_boton2)
boton3 = tk.Button(ventana, text="Botón 3", command=accion_boton3)
boton4 = tk.Button(ventana, text="Botón 4", command=accion_boton4)
boton_ingresar_texto = tk.Button(ventana, text="Ingresar Texto", command=ingresar_texto)

# Colocar los botones en la ventana
boton1.grid(row=0, column=0, padx=10, pady=10)
boton2.grid(row=1, column=0, padx=10, pady=10)
boton3.grid(row=2, column=0, padx=10, pady=10)
boton4.grid(row=3, column=0, padx=10, pady=10)

# Ejecutar el bucle principal
ventana.mainloop()

