import sqlite3

# Conectar a la base de datos, si no existe se creará
conn = sqlite3.connect('mi_base_de_datos.db')

# Crear un cursor
c = conn.cursor()

# Crear una tabla
c.execute('''
    CREATE TABLE mi_tabla (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        edad INTEGER
    )
''')

# Guardar (commit) los cambios
conn.commit()

# Cerrar la conexión a la base de datos
conn.close()

