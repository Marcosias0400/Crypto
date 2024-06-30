# Motor de Busqueda
import sqlite3
# Para poder hacer los esquemas de ingreso de registros
from Cripto import *
from cryptography.hazmat.primitives import serialization
import uuid 

# Clase que agrupa todas las herramientas de bases de datos
class herramientas_BD:
  # Constructor
  def __init__(self, base_admin, base_donantes, clave_sim, clave_privada, clave_publica):
    # existen dos bases de datos 
    # la de administradores y la de donantes
    self.administradores = base_admin
    self.donantes        = base_donantes
    self.campo_protegido = ["cuenta_bancaria", "concepto", "direccion"]
    self.C               = herramientas_criptograficas(clave_sim, clave_privada, clave_publica)
    
  # La base de datos de administradores debe tener al menos un registro  
  def instancia_admin(self):
    # Conectar a la base de datos, si no existe se creará
    conn = sqlite3.connect(self.administradores)

    # Crear un cursor
    c = conn.cursor()

    # Crear una tabla solo si no existe
    c.execute('''
        CREATE TABLE IF NOT EXISTS adminitradores (
        id TEXT PRIMARY KEY,
        permiso INT,
        firma TEXT
        )
        ''')
    
    # Insertar un registro en la tabla
    # El administrador 'root' es el unico con permiso 0
    c.execute('''INSERT INTO adminitradores (id, permiso, firma) VALUES (?, ?, ?)''', ('root', 0,self.C.firmado('holamundo')))
    
    # Guardar (commit) los cambios
    conn.commit()
    
    # Cerrar la conexión a la base de datos
    conn.close()
  
  # El unico que puede aggregar administradores es el usuario root
  def add_admin(self, id_admin, frase):
    # Conectar a la base de datos, si no existe se creará
    conn = sqlite3.connect(self.administradores)

    # Crear un cursor
    c = conn.cursor()

    # Insertar un registro en la tabla
    # el resto de los administraodres tienen permiso 1
    c.execute('''INSERT INTO adminitradores (id, permiso, firma) VALUES (?, ?, ?)''', (id_admin, 1, self.C.firmado(frase)))
    
    # Guardar (commit) los cambios
    conn.commit()
    
    # Cerrar la conexión a la base de datos
    conn.close()
  
  # el unico que puede quitar administradores es el usuario root
  def rm_admin(self, id_admin):
    # Crea una conexion
    conn = sqlite3.connect('mi_base_de_datos.db')
    
    # Crea un cursor
    c = conexion.cursor()

    # Quita al admin
    consulta = """DELETE FROM administradores WHERE id = {id_admin}"""
    c.execute(consulta)
    conn.commit()
    c.close()
    conn.close()
  
  # Agregar registros a la tabla de donantes
  def add_donantes(self, ingreso):
    # Conectar a la base de datos, si no existe se creará
    conn = sqlite3.connect(self.donantes)

    # Crear un cursor
    c = conn.cursor()

    # Crear una tabla solo si no existe
    c.execute('''CREATE TABLE IF NOT EXISTS donantes (cuenta_bancaria TEXT PRIMARY KEY,
             nombre TEXT,apellido1 TEXT, apellido2 TEXT, 
             concepto TEXT, tier INT, direccion TEXT)
        ''')
    # Ingresa los datos a traves de la lista 
    c.execute('''INSERT INTO donantes (cuenta_bancaria, 
                                       nombre, apellido1, apellido2,
                                       concepto, tier, direccion) 
                                       VALUES (?, ?, ?, ?, ?, ?, ?)''', (self.C.cif(ingreso[0]), 
                                       self.C.cif(ingreso[1]), self.C.cif(ingreso[2]), self.C.cif(ingreso[3]),
                                       self.C.cif(ingreso[4]), ingreso[5], self.C.cif(ingreso[6])))

    # Guardar (commit) los cambios
    conn.commit()

    # Cerrar la conexión a la base de datos
    conn.close()


  # El unico que puede quitar donantes es el administrador 'root' 
  def rm_donante(self, cuanta_bancaria):
    # Conectar a la base de datos, si no existe se creará
    conn = sqlite3.connect(self.donantes)

    # Crear un cursor
    c = conn.cursor()

    # Ingresa los datos a traves de la lista 
    consulta = """DELETE FROM donantes WHERE cuenta_bancaria = {self.C.cif(cuenta_bancaria)}"""

    c.execute(consulta)
    
    # Guardar (commit) los cambios
    conn.commit()
    
    c.close()
    # Cerrar la conexión a la base de datos
    conn.close()
  
  # Hacer busquedas por campo
  def query_single(self, campo, busqueda):
    conn = sqlite3.connect(self.donantes)
    c = conn.cursor()

    consulta = f"""SELECT * FROM donantes WHERE {campo} = '{self.C,cif(busqueda)}'"""
    
    c.execute(consulta)
    
    resultados = c.fetchall()
    
    c.close()
    # Cerrar la conexión a la base de datos
    conn.close()
    return resultados
  
  # Hacer busquedas multipcampo
  def query_multiple(self, campos, busquedas):
    conn = sqlite3.connect(self.donantes)
    c = conn.cursor()
    multi=f""
    n=len(campos)
    for i in range(n):
      if i>0:
        multi+= f"AND {campos[i]} = '{busquedas[i]}'"
      else:
        multi+= f"{campos[i]} = '{busquedas[i]}'"
    consulta = """SELECT * FROM donantes WHERE """ + multi
    c.execute(consulta)
    resultados = c.fetchall()
    c.close()
    # Cerrar la conexión a la base de datos
    conn.close()
    return resultados
  
  
