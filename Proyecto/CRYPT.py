# Fernet es una forma abreviada de decir AES 256 
from cryptography.fernet import Fernet
# Importa todos los tipos de padding del submodulo de cifrado asimetrico
from cryptography.hazmat.primitives.asymmetric import padding
# el backend se usa para instanciar la funcion hash
from cryptography.hazmat.backends import default_backend
# importa los hashes ya hechos, aun que solo se usa SHA256
from cryptography.hazmat.primitives import hashes

class herramientas_criptograficas:
  # Concentra todas las herramientas criptograficas usadas en el 
  # proyecto, requiere tres archivos generados con OpenSSL
  def __init__(self, clave_AES, clave_priv, clave_pub):
    self.clave_simetrica=clave_AES
    self.clave_priv=clave_priv
    self.clave_pub=clave_pub
  
  # funcion de cifrado
  def cif(self, texto_llano):
    # Fernet es el cifrador usa AES 256
    # con el modo cbc
    cifrador = Fernet(self.clave_simetrica)
    # el texto llano tiene que ser tratado como bits
    bits = texto_llano.encode('utf-8')
    # retorna los datos encriptados
    return cifrador.encrypt(bits)
  
  # Funcion de decifrado  
  def dcif(self, texto_cif):
    # Siempre se usa el cifrador
    cifrador = Fernet(self.clave_simetrica)
    td=cifrador.decrypt(texto_cif)
    return td.decode('utf-8')
  
  # funcion que retorna el hash
  def Hash_mio(self, texto_llano):
    # Para no guardar la frase de seguridad
    # Objeto Hasheador
    Hash = hashes.Hash(hashes.SHA256(), backend=default_backend())
    # Agrega los datos al hasher
    bits=texto_llano.encode('utf-8')
    Hash.update(bits)
    # da el valor del hash los datos
    return Hash.finalize()

  # Fuincion de firmado con RSA   
  def firmado(self, texto_a_firmar):
    # devuelve la firma
    # PARAMETROS
    #                           Texto que se firma
    #                                           Se usa un padding, en este caso MGFG1 
    #                                                                                          Parametro de salt
    #                                                                                                                                Usa SHA256 para verificar integridad
    x = self.Hash_mio(texto_a_firmar)
    return self.clave_priv.sign(x, padding.PSS(mgf=padding.MGF1(hashes.SHA256()) , salt_length=padding.PSS.MAX_LENGTH) , hashes.SHA256() )
  
  # Funcion de verificado  
  def verificado(self, firma, texto_a_verificar):
    # Intenta primero con la clave publica
    try:
    # PARAMETROS:
    #                       firma: esto si se guarda en la BD 
    #                              texto firmado: esto se ingresa el la iterfaz grafica
    #                                                  paddig o relleno
    #                                                                                                  parametro de salt 
    #                                                                                                                                       Usa SHA256 para verificar integridad
      x=self.Hash_mio(texto_a_verificar)
      self.clave_pub.verify(firma, x , padding.PSS(mgf=padding.MGF1(hashes.SHA256()) , salt_length=padding.PSS.MAX_LENGTH) , hashes.SHA256())
      return 1
    except:
      return 0
     
