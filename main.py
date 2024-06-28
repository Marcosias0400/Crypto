import tkinter as tk
from admin_app import AdminApp
from database_utils import DatabaseUtils
from crypto_utils import CryptoUtils
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Función para cargar la clave privada desde un archivo .pem
def load_private_key(file_path):
    with open(file_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None
        )
    return private_key

# Función para cargar la clave pública desde un archivo .pem
def load_public_key(file_path):
    with open(file_path, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read()
        )
    return public_key

# Cargar las claves RSA
private_key = load_private_key("private_key.pem")
public_key = load_public_key("public_key.pem")

# Generar una clave AES simétrica
aes_key = b'32_byte_key_for_aes_encryption____'  # Clave AES de 32 bytes (256 bits)

# Crear instancia de CryptoUtils
crypto_utils = CryptoUtils(aes_key, private_key, public_key)

# Crear instancia de DatabaseUtils
database_utils = DatabaseUtils(crypto_utils)

# Crear la aplicación principal de Tkinter
root = tk.Tk()

# Crear instancia de AdminApp
app = AdminApp(root, database_utils, crypto_utils)

