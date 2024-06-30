import tkinter as tk
from tkinter import ttk

def mostrar_tabla(datos):
    ventana = tk.Tk()
    ventana.title("Tabla de Datos")
    ventana.geometry("400x300")

    # Crear el widget Treeview
    tree = ttk.Treeview(ventana, columns=[str(i) for i in range(len(datos[0]))], show='headings')

    # Configurar las columnas
    for i in range(len(datos[0])):
        tree.heading(str(i), text=f"Columna {i+1}")
        tree.column(str(i), anchor=tk.CENTER)

    # Agregar los datos a la tabla
    for fila in datos:
        tree.insert("", tk.END, values=fila)

    # Colocar el Treeview en la ventana
    tree.pack(expand=True, fill=tk.BOTH)

    # Ejecutar el bucle principal
    ventana.mainloop()

# Ejemplo de uso
datos = [
    [1, 'Alice', 24],
    [2, 'Bob', 30],
    [3, 'Charlie', 22],
    [4, 'Diana', 27]
]

mostrar_tabla(datos)

