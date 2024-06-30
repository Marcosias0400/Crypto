from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Genera una clave privada RSA
clave_privada = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
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

# Obtén la clave pública
clave_publica = clave_privada.public_key()

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

