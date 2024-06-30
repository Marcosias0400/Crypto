# Fernet es una forma abreviada de decir AES 256 
from cryptography.fernet import Fernet

# Lee la clave desde un archivo
with open('clave.key', 'rb') as archivo_clave:
    clave = archivo_clave.read()

# Crea una instancia de Fernet usando la clave
fernet = Fernet(clave)

# Datos a encriptar
datos = b"datos secretos"

# Encripta los datos
datos_encriptados = fernet.encrypt(datos)
print("Datos encriptados:", datos_encriptados)

# Desencripta los datos
datos_desencriptados = fernet.decrypt(datos_encriptados)
print("Datos desencriptados:", datos_desencriptados)

