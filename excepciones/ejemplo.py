class MiExcepcion(Exception):
    def __init__(self, err):
        print(f"Por favor intentelo nuevamente :)")


# def sumar():
    # while True:
        # Pidiendo números
       # a = input("Digite un numero: ")
       # b = input("Digite otro numero: ")
        # Intentando convertirlos a enteros y sumarlos
       # try:
        # resultado = int(a) + int(b)
        # MiExcepcion()
        # Mostrando una excepcion
        # "Except" no se ejecuta a menos que haya una excepcion en "try"
        # except MiExcepcion as e:
        # print("Te pedi un número, ayote, no te hagas el gracioso")
        # Con el "type(e).__name__" estamos haciendo que el programa nos muestre
        # print(f"Eror: {type(e).__name__}")
        # El nombre del error. Si solamente se invoca la función, en lugar de mostrarse el error en la pantalla del
        # Código, será en la temrinal, en forma de un print
        # except ZeroDivisionError: #Se usa cuando no queremos que se divida por cero
        # else:
        #   break
        # El finally se ejecuta siempre
        # finally:
        #   print("Esto se ejecuta siempre")
    # return resultado

#
# print(sumar())

# El "try" sirve para decirle al programa que cosa hacer en caso de una excepcion
