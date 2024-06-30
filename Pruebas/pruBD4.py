import sqlite3

conexion = sqlite3.connect('mi_base_de_datos.db')
cursor = conexion.cursor()

consulta = """
DELETE FROM mi_tabla
WHERE id = 1
"""

cursor.execute(consulta)
conexion.commit()
cursor.close()
conexion.close()

