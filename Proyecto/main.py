from SQL import herramientas_BD
from CRYPT import herramientas_criptograficas
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from GUI import AdminLogin

if __name__ == "__main__":
  # Se necesitan estos parametros
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

  with open('clave.key', 'rb') as archivo_clave:
    clave_sim = archivo_clave.read()

  # Crear instancia de herramientas de base de datos
  db = herramientas_BD("admin_db.sqlite", "donantes_db.sqlite", clave_sim, clave_privada, clave_publica)

  # Inicializar base de datos
  db.instancia_admin()

  # Iniciar interfaz de inicio de sesión
  app = AdminLogin(db)
  app.mainloop()

