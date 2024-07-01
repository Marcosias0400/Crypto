import tkinter as tk
from tkinter import messagebox
import sys
from Cripto import *
from SQL import *

# Clase que estructura toda la interaccion con una persona
class Interfaz_Grafica:
  # Constructor o arbol de ventanas
  def __init__(self, base_admin, base_donantes, clave_sim, clave_privada, clave_publica):
    # Ventana padre de todo el programa 
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    self.ventana_seleccion = tk.Tk()
    self.basesDatos=herramientas_BD(base_admin, base_donantes, clave_sim, clave_privada, clave_publica)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  
  def ventana_inicial(self):
    self.basesDatos.instancia_admin()
    self.ventana_seleccion.title("Seleccion de ingreso")
    self.ventana_seleccion.geometry("150x100")

    # Crear y configurar los botones con comandos adecuados
    boton_admn = tk.Button(self.ventana_seleccion, text="Administracion", command=self.acceso_admin)
    boton_user = tk.Button(self.ventana_seleccion, text="Consultante", command=self.consultante)
    boton_admn.pack(pady=10)
    boton_user.pack(pady=10)
    self.ventana_seleccion.mainloop()
  
  def acceso_admin(self):
    # Crear y mostrar la ventana de administración aquí
    self.ventana_acceso_admin = tk.Toplevel(self.ventana_seleccion)
    self.ventana_seleccion.withdraw()
    self.ventana_acceso_admin.title("Acceso") 
    self.ventana_acceso_admin.geometry("300x200")
    
     # Define la cuadrícula (2 filas, 3 columnas)
    self.ventana_acceso_admin.rowconfigure(0, weight=1)
    self.ventana_acceso_admin.rowconfigure(1, weight=1)
    self.ventana_acceso_admin.rowconfigure(2, weight=1)
    self.ventana_acceso_admin.columnconfigure(0, weight=1)
    self.ventana_acceso_admin.columnconfigure(1, weight=1)
    self.ventana_acceso_admin.columnconfigure(2, weight=1)
    
    
    tk.Label(self.ventana_acceso_admin, text="Admin ID:").grid(row=0, column=0, padx=10, pady=10)
    self.admin_id_entrada = tk.Entry(self.ventana_acceso_admin)
    self.admin_id_entrada.grid(row=0, column=1, padx=10, pady=10)
        
    tk.Label(self.ventana_acceso_admin, text="Password:").grid(row=1, column=0, padx=10, pady=10)
    self.admin_frase_entrada = tk.Entry(self.ventana_acceso_admin, show='*')
    self.admin_frase_entrada.grid(row=1, column=1, padx=10, pady=10)
        
    tk.Button( self.ventana_acceso_admin, text="Accesa", command=self.validacionAcceso).grid(row=2, columnspan=1, pady=10)
    tk.Button( self.ventana_acceso_admin, text="Retorna", command=lambda:self.volver_a_ventana_seleccion(self.ventana_acceso_admin)).grid(row=2, columnspan=2, pady=10)
   
    # Aquí es donde vinculamos el evento de cierre de la ventana a la función de salida
    self.ventana_acceso_admin.protocol("WM_DELETE_WINDOW", self.salir)
  
  def validacionAcceso(self):
    admin_id = self.admin_id_entrada.get()
    frase    = self.admin_frase_entrada.get()
    admins=self.basesDatos.query_admin(admin_id)
    print(admins)
    if admins[0] == admin_id:
      return True
    else:
      return False
  
  def salir(self):
    sys.exit()
  
  def volver_a_ventana_seleccion(self, ventana):
    ventana.destroy()  # Cerrar la ventana principal
    self.ventana_seleccion.deiconify()  # Mostrar la ventana de acceso nuevamente
      
  def usr_query(self, busqueda):
    self.ventana_resultados=tk.Toplevel(self.ventana_seleccion_consulta_usr)
    self.ventana_seleccion_consulta_usr.withdraw()
    if len(busqueda)==1:
      res=self.basesDatos.query_single(busqueda[0], busqueda[1:])
    else:
      res=self.basesDatos.query_multiple(busqueda[0], busqueda[1:])
    
    
  def mostrar_entrada(self, entradas):
    entrada = tk.Entry(self.ventana_seleccion_consulta_usr)
    entrada.pack(pady=10)
    entradas.append(entrada)
  
  def consultante(self):
    self.ventana_seleccion_consulta_usr = tk.Toplevel(self.ventana_seleccion)
    self.ventana_seleccion.withdraw()
    self.ventana_seleccion_consulta_usr.title("Busqueda") 
    self.ventana_seleccion_consulta_usr.geometry("900x600")
    label_bienvenida = tk.Label(self.ventana_seleccion_consulta_usr, text="¡Bienvenido al portal de transparencia de <ONG>!")
    label_bienvenida.pack(pady=20)

    # Crea un diccionario para almacenar los campos de texto
    self.text_fields = {}

    # Crea una lista de nombres de botones
    button_names = ["Nombre", "Apellido Paterno", "Apellido Materno", "Rango"]
    inputs=[]
    # Crea un frame y un botón para cada nombre en la lista
    for name in button_names:
      frame = tk.Frame(self.ventana_seleccion_consulta_usr)
      frame.pack(pady=10, anchor='w')
      button = tk.Button(frame, text=name, command=self.mostrar_entrada(inputs))
      button.pack(side=tk.LEFT)
    
    # Agrega un botón para obtener el texto de los campos de texto
    boton_obtener_texto = tk.Button(self.ventana_seleccion_consulta_usr, text="Busqueda", command=self.usr_query)
    boton_obtener_texto.pack(pady=10)
    # En el método `consultante`, después de crear el botón "Obtener texto":
    texto_boton = boton_obtener_texto.text

    
    # Crea un frame para el botón de retorno y lo coloca en la esquina inferior derecha
    frame_retorno = tk.Frame(self.ventana_seleccion_consulta_usr)
    frame_retorno.pack(side=tk.BOTTOM, fill=tk.X)
    boton_retorno = tk.Button(frame_retorno, text="Volver", command=self.volver_a_ventana_seleccion(self.ventana_seleccion_consulta_usr))
    boton_retorno.pack(side=tk.RIGHT)
    
    # Aquí es donde vinculamos el evento de cierre de la ventana a la función de salida
    self.ventana_seleccion_consulta_usr.protocol("WM_DELETE_WINDOW", self.salir)
      
  
    
  
  
