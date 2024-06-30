import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('mi_base_de_datos.db')

# Crear un cursor
c = conn.cursor()

# Insertar un registro en la tabla
c.execute('''
    INSERT INTO mi_tabla (id, nombre, edad)
    VALUES (?, ?, ?)
''', (4, 'Juan', 20))

# Guardar (commit) los cambios
conn.commit()

# Cerrar la conexión a la base de datos
conn.close()

