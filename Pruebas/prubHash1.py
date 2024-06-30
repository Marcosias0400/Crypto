from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

# Define los datos a hashear
data = b"my secret data"

# Crea un hasher
digest = hashes.Hash(hashes.SHA256(), backend=default_backend())

# Agrega los datos al hasher
digest.update(data)

# Finaliza el hash y obtén el digest de los datos
hash_value = digest.finalize()

# Imprime los datos hasheados
print(f"El hash de los datos es: {hash_value}")

