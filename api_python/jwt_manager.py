# Immportando libreria que genera el token
from jwt import encode, decode


#Creando método para generar token
def create_token(data: dict):  #Información que se convertirá en token
    #Llamar encode, recibe payload que corresponde a data, clave secreta y algoritmo de encriptación
    token: str = encode(payload=data, key="my_secret_key", algorithm="HS256")
    return token


def validate_token(token: str) -> dict:
    data: dict = decode(token, key="my_secret_key", algorithms=['HS256'])
    return data
