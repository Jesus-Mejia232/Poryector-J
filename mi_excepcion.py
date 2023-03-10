class MiExcepcion(Exception):
    def __init__(self, err):
        print(f"Acaba de ocurrir un error")


def sumar():
    while True:
        a = input("Digite un número: ")
        b = input("Digite otro número: ")
        try:
            resultado = int(a) + int(b)
        except:
            print(f"Acaba de ocurrir un excepcion: {MiExcepcion}")
        finally:
            print("Fin del programa")


print(sumar())
