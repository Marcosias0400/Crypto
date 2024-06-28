import sqlite3

class DatabaseUtils:
    def __init__(self, crypto_utils):
        self.crypto_utils = crypto_utils
        self.create_admin_table()
        self.create_donantes_table()
        self.add_default_admin()

    def create_admin_table(self):
        conn = sqlite3.connect('admin.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS admin (
                            admin_id TEXT PRIMARY KEY,
                            password TEXT NOT NULL,
                            permission INTEGER NOT NULL
                          )''')
        conn.commit()
        conn.close()

    def add_admin(self, admin_id, password, permission):
        hashed_password = self.crypto_utils.hash_password(password)
        encrypted_password = self.crypto_utils.rsa_encrypt(hashed_password)
        conn = sqlite3.connect('admin.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO admin (admin_id, password, permission) VALUES (?, ?, ?)', 
                       (admin_id, encrypted_password, permission))
        conn.commit()
        conn.close()

    def delete_admin(self, admin_id):
        conn = sqlite3.connect('admin.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM admin WHERE admin_id = ?', (admin_id,))
        conn.commit()
        conn.close()

    def validate_admin_login(self, admin_id, password):
        conn = sqlite3.connect('admin.db')
        cursor = conn.cursor()
        cursor.execute('SELECT password, permission FROM admin WHERE admin_id = ?', (admin_id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        if result:
            encrypted_password, permission = result
            decrypted_password = self.crypto_utils.rsa_decrypt(encrypted_password)
            if decrypted_password == self.crypto_utils.hash_password(password):
                return True, permission
        return False, None

    def create_donantes_table(self):
        conn = sqlite3.connect('donantes.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS donantes (
                            id INTEGER PRIMARY KEY,
                            nombre TEXT NOT NULL,
                            apellido1 TEXT NOT NULL,
                            apellido2 TEXT,
                            donacion BLOB,
                            tier INTEGER,
                            cuenta_bancaria BLOB,
                            direccion BLOB
                          )''')
        conn.commit()
        conn.close()

    def add_donante(self, nombre, apellido1, apellido2, donacion, tier, cuenta_bancaria, direccion):
        conn = sqlite3.connect('donantes.db')
        cursor = conn.cursor()
        
        # Cifrar los datos antes de insertar en la base de datos
        encrypted_donacion = self.crypto_utils.aes_encrypt(str(donacion))
        encrypted_cuenta_bancaria = self.crypto_utils.aes_encrypt(cuenta_bancaria)
        encrypted_direccion = self.crypto_utils.aes_encrypt(direccion)
        
        cursor.execute('INSERT INTO donantes (nombre, apellido1, apellido2, donacion, tier, cuenta_bancaria, direccion) VALUES (?, ?, ?, ?, ?, ?, ?)', 
                       (nombre, apellido1, apellido2, encrypted_donacion, tier, encrypted_cuenta_bancaria, encrypted_direccion))
        
        conn.commit()
        conn.close()

    def get_donantes(self):
        conn = sqlite3.connect('donantes.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM donantes')
        donantes = cursor.fetchall()
        conn.close()
        
        # Descifrar los datos recuperados de la base de datos
        decrypted_donantes = []
        for donante in donantes:
            id, nombre, apellido1, apellido2, donacion, tier, cuenta_bancaria, direccion = donante
            decrypted_donacion = self.crypto_utils.aes_decrypt(donacion)
            decrypted_cuenta_bancaria = self.crypto_utils.aes_decrypt(cuenta_bancaria)
            decrypted_direccion = self.crypto_utils.aes_decrypt(direccion)
            decrypted_donantes.append((id, nombre, apellido1, apellido2, decrypted_donacion, tier, decrypted_cuenta_bancaria, decrypted_direccion))
        
        return decrypted_donantes

    def get_donante_by_id(self, donante_id):
        try:
            self.cursor.execute("SELECT * FROM donantes WHERE id = ?", (donante_id,))
            donante_data = self.cursor.fetchone()
            if donante_data:
                # Desencriptar los campos cifrados
                nombre = self.crypto_utils.aes_decrypt(donante_data[1])
                apellido1 = self.crypto_utils.aes_decrypt(donante_data[2])
                apellido2 = self.crypto_utils.aes_decrypt(donante_data[3])
                donacion = self.crypto_utils.aes_decrypt(donante_data[4])
                tier = self.crypto_utils.aes_decrypt(donante_data[5])
                cuenta_bancaria = self.crypto_utils.aes_decrypt(donante_data[6])
                direccion = self.crypto_utils.aes_decrypt(donante_data[7])
                
                return {
                    'id': donante_data[0],
                    'nombre': nombre,
                    'apellido1': apellido1,
                    'apellido2': apellido2,
                    'donacion': donacion,
                    'tier': tier,
                    'cuenta_bancaria': cuenta_bancaria,
                    'direccion': direccion
                }
            else:
                print(f"Donante con ID {donante_id} no encontrado.")
                return None
        except sqlite3.Error as e:
            print(f"Error al obtener el donante con ID {donante_id}: {e}")
            return None

    def add_default_admin(self):
        conn = sqlite3.connect('admin.db')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM admin WHERE admin_id = "root"')
        count = cursor.fetchone()[0]
        if count == 0:
            self.add_admin('root', 'holamundo', 0)
        cursor.close()
        conn.close()

