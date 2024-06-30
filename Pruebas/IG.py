import tkinter as tk
from tkinter import messagebox
from Cripto import *
from SQL import *

# Clase que estructura toda la interaccion con una persona
class Interfaz_Grafica:
  # Constructor o arbol de ventanas
  def __init__(self):
    # Ventana padre de todo el programa 
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    self.ventana_seleccion = tk.Tk()
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  
  def volver_a_ventana_seleccion(self):
    ventana_seleccion_consulta_usr.destroy()  # Cerrar la ventana principal
    self.ventana_seleccion.deiconify()  # Mostrar la ventana de acceso nuevamente
      
  def acceso_admin(self):
    # Crear y mostrar la ventana de administración aquí
    print('Hola admin')

  def consultante(self):
    # Crear y mostrar la ventana de consulta aquí, se va a conculatar por 4 campos:
    # Nombre, apellido paterno, apellido materno, Rango de donacion
    ventana_seleccion_consulta_usr = tk.Toplevel(self.ventana_seleccion)
    # Oculta la ventana anterior
    self.ventana_seleccion.withdraw()
    # Nombre de la vantana
    ventana_seleccion_consulta_usr.title("Busqueda") 
    # Geometria de la ventana
    ventana_seleccion_consulta_usr.geometry("300x200")
    label_bienvenida = tk.Label(ventana_seleccion_consulta_usr, text="¡Bienvenido al portal de transparencia de <ONG>! \n Haz un consulta")
    label_bienvenida.pack(pady=20)

    boton_cerrar = tk.Button(ventana_seleccion_consulta_usr, text="Cerrar", command=ventana_seleccion_consulta_usr.destroy)
    boton_cerrar.pack(pady=10)

    boton_retorno = tk.Button(ventana_seleccion_consulta_usr, text="Volver", command=self.volver_a_ventana_seleccion)
    boton_retorno.pack(pady=10) 
    
    print('Hola user')
      
  def ventana_inicial(self):
    self.ventana_seleccion.title("Seleccion de ingreso")
    self.ventana_seleccion.geometry("300x200")

    # Crear y configurar los botones con comandos adecuados
    boton_admn = tk.Button(self.ventana_seleccion, text="Administracion", command=self.acceso_admin)
    boton_user = tk.Button(self.ventana_seleccion, text="Consultante", command=self.consultante)
    boton_admn.pack(pady=10)
    boton_user.pack(pady=10)
    self.ventana_seleccion.mainloop()
    
  
  
