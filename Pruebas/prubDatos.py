from SQL import *
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
  
  # Instancia con la llave simetrica
with open('clave.key', 'rb') as archivo_clave:
  clave_sim = archivo_clave.read()
  
BD=herramientas_BD("admin.db","don.db", clave_sim, clave_privada, clave_publica)
BD.instancia_admin()
BD.add_admin('Juan', '1234')
BD.add_admin('Pedro', '4321')
x=["12345", "Pedro", "Martinez", "Armendariz", "1234.98", 2, "Ecatepec de Morelos"]
y=["18305", "Pedro", "Rodriguez", "Lopez", "500.5", 1, "ciudad del vaticano"]
z=["12305", "Mario", "Rodriguez", "Nagera", "20", 0, "Ingoshima"]
BD.add_donantes(x)
BD.add_donantes(y)
BD.add_donantes(z)
print(BD.query_single("nombre", "Pedro"))
print("\n")
print(BD.query_single("apellido1", "Rodriguez"))
print("\n")
print(BD.query_multiple(["nombre", "apellido2"], ["Pedro", "Armendariz"]))
