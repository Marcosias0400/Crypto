import sqlite3
from CRYPT import herramientas_criptograficas

class herramientas_BD:
    def __init__(self, db_admin_path, db_donantes_path, clave_sim, clave_privada, clave_publica):
        self.db_admin_path = db_admin_path
        self.db_donantes_path = db_donantes_path
        self.C = herramientas_criptograficas(clave_sim, clave_privada, clave_publica)
        self.iniciar_bd()

    def iniciar_bd(self):
        self.conn_admin = sqlite3.connect(self.db_admin_path)
        self.conn_donantes = sqlite3.connect(self.db_donantes_path)

    def instancia_admin(self):
        c = self.conn_admin.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS administradores (
                id TEXT PRIMARY KEY,
                permiso INTEGER,
                firma TEXT
            )
        ''')
        # Verificar si el administrador root ya existe
        c.execute('SELECT * FROM administradores WHERE id = ?', ('root',))
        if not c.fetchone():
            c.execute('''INSERT INTO administradores (id, permiso, firma) VALUES (?, ?, ?)''', 
                      ('root', 0, self.C.firmado('holamundo')))
        self.conn_admin.commit()

    def query_admin(self):
        c = self.conn_admin.cursor()
        c.execute('SELECT * FROM administradores')
        return c.fetchall()

    def add_admin(self, admin_id, security_phrase):
        firma = self.C.firmado(security_phrase)
        c = self.conn_admin.cursor()
        c.execute('''INSERT INTO administradores (id, permiso, firma) VALUES (?, ?, ?)''', 
                  (admin_id, 1, firma))
        self.conn_admin.commit()

    def rm_admin(self, admin_id):
        c = self.conn_admin.cursor()
        c.execute('DELETE FROM administradores WHERE id = ?', (admin_id,))
        self.conn_admin.commit()

    def add_donantes(self, donor_info):
        c = self.conn_donantes.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS donantes (
                cuenta_bancaria TEXT,
                nombre TEXT,
                apellido1 TEXT,
                apellido2 TEXT,
                concepto TEXT,
                tier TEXT,
                direccion TEXT
            )
        ''')
        # Encriptar los datos del donante
        donor_info_encrypted = [self.C.cif(dato) for dato in donor_info]
        c.execute('''INSERT INTO donantes (cuenta_bancaria, nombre, apellido1, apellido2, concepto, tier, direccion) 
                     VALUES (?, ?, ?, ?, ?, ?, ?)''', donor_info_encrypted)
        self.conn_donantes.commit()

    def query_usr(self):
        c = self.conn_donantes.cursor()
        c.execute('SELECT * FROM donantes')
        rows = c.fetchall()
        # Desencriptar los datos del donante
        decrypted_rows = []
        for row in rows:
            decrypted_row = [self.C.dcif(dato) for dato in row]
            decrypted_rows.append(decrypted_row)
        return decrypted_rows

