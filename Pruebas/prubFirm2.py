from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

# Cargar la clave privada desde un archivo
with open("priv.key", "rb") as key_file:
    clave_privada = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )

# Datos a firmar
datos = b"datos a firmar"

# Firmar los datos
firma = clave_privada.sign(
    datos,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# Cargar la clave pública desde un archivo
with open("pub.key", "rb") as key_file:
    clave_publica = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )

# Verificar la firma
try:
    clave_publica.verify(
        firma,
        datos,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("La firma es válida.")
except:
    print("La firma no es válida.")


