# Creando una lista (se puede modificar)
lista = ["Jesus Edgardo", "Algo por aquí", True, 1.69]

# Creado una tupla (no se puede modigicar)
tupla = ("Jesus Edgardo", "Algo por aquí", True, 1.69)
# La tupla usa parentesis, y las lista usa los parentesis []
# Los diccionarios(dict) usan las llaves {}

# Esto es valido
lista[2] = "Otro tipo de dato distinto"

print(lista[1])

"""
Creando un conjunto (set) (Son básicamente, tuplas, pero desordenadas). Se puede 
Reconstruir, pero cada elemento no lo podemos modificar en particular, lo mismo
Para las tuplas.

No se acceder por indices, no almacena datos duplicados"""

conjunto = {"Jesus Edgardo", "Algo por aquí", True, 1.69}


# Creando un diccionario (dict) (Se accede a los indices con cadenas de texto)
"""La estructura del diccionario es (Clave : Valor, y separamos con comas)"""

diccionario = {
    # Clave   | Valor
    'Nombre': "Jesus Mejia",
    'Edad': 16,
    'Altura': "1.69"
}

print(diccionario["Altura"])
print(lista[3])
