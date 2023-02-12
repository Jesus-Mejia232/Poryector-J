numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Creando una función lamnda para multiplicar por dos


def multiplicando_numeros(x): return x*2

# Creando función común que diga que es par o no

"""
def es_par(numero):
    if (numero % 2 == 0):
        return True


# Creando filter con una funcion común
numeros_pares = filter(es_par, numeros)
# Convertirlo a lista para ver el resultado de forma correcta, es decir, que la funcion muestre una lista de los caracteres que son pares
print(list(numeros_pares))
"""

# Todo el código de funciones de arriba, se simplifica con lambda creando lo mismo, pero con lambda
numeros_pares = filter(lambda numero: numero % 2 == 0, numeros)
# Cambiar la varible a lista para que se imprima en pantalla la lista de todos los números pares
print(list(numeros_pares))
