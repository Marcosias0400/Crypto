import sqlite3

conexion = sqlite3.connect('mi_base_de_datos.db')
cursor = conexion.cursor()

consulta = """
SELECT * FROM mi_tabla
WHERE nombre = 'Juan'
"""

cursor.execute(consulta)

resultados = cursor.fetchall()

for cliente in resultados:
  print(f"ID: {cliente[0]} | Nombre: {cliente[1]} | Edad: {cliente[2]}")

cursor.close()
conexion.close()

