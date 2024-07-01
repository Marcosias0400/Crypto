# Prueba de construccion
from IG import *
with open("priv.key", "rb") as key_file:
  clave_privada = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )
  
with open("pub.key", "rb") as key_file:
  clave_publica = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )
  
  # Instancia con la llave simetrica
with open('clave.key', 'rb') as archivo_clave:
  clave_sim = archivo_clave.read()
X=Interfaz_Grafica('admin.db', 'don.db', clave_sim, clave_privada, clave_publica)
X.ventana_inicial()
X.salir()
