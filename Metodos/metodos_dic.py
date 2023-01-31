diccionario = {
    "Nombre" : 'Jesus',
    "Apellido" : 'Mejía',
    "ingresianual" : 10
}

#Keys, sirve para crear una tupla de los elementos

claves = diccionario.keys()

#Get obteniendo un valor de un programa, (si no encuentra nada, el programa continua)
claves = diccionario.get("Goku")

#Eliminando elementos del diccionario con pop
eliminando_elementos = diccionario.pop("Nombre")

print(eliminando_elementos)

#Obteniendo un elemento dict_item iterable 
diccionario_iterable = diccionario.items()

print(diccionario_iterable)