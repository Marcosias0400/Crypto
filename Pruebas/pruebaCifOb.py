from cryptography.hazmat.primitives import serialization
from Cripto import *
texto='hola mundo'
#=========================================================================
# Esto va en el progrma principal
# Instacia con las llaves de RSA
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
    
C=herramientas_criptograficas(clave_sim, clave_privada, clave_publica)
#======================================================================
print('texto hasheado', C.Hash_mio(texto))
print('texto cifrado', C.cif(texto))
print('texto decifrado', C.dcif(C.cif(texto)))
y=C.firmado(texto)
print('texto firmado', y)
print('texto verificado',C.verificado(y,texto))
print('texto no verificado',C.verificado(texto,texto))
