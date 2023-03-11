class MiExcepcion(Exception):
    def __init__(self, err):
        print(f"Por favor intentelo nuevamente :)")


raise MiExcepcion("No se realemente cual es el objetico de este comentario")

try:
    raise MiExcepcion("jaja persona goku")
except:
    print("Como vas a comerte ese tipo de error")


# Con esto básicamente estamos predefiniendo que nos va a decir el programa en caso de llegar a asignar este tipo de
# Excepcion
