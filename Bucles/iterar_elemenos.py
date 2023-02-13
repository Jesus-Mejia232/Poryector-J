"""Qué iterar, es recorrer un element en pedazitos, esos 
pedazitos y la forma en la que se van a ir salteando la define un 
iterador"""

animales = {"Perro", "Gato", "Tortutornado", "Cocodrilo"}
numeros = {12, 32, 33, 45, 67, 22}

for animal in animales:
    print(animal)

for num in numeros:
    resultado = num * 10
    print(resultado)


# Para poder iterar dos conjuntos a la vez, ambas conjuntos deben tener la misma cantidad de elementos
for numer, ani in zip(animales, numeros):
    # El orden en el que itera los elementos, es: Primero conjunto1 luego conjunto 2
    print(f'Recorrriendo datos conjunto 1: {numer}')
    # En ese orden hasta que terminen los elememtos de la conjunto
    print(f'Recorrriendo datos conjunto 2: {ani}')

# Iterar conjuntos con rangel()

# Se definen dos parametros, el primero define donde arranca, el segundo donde termina
for num in range(10, 21):
    # Si solo le pasamos un parametro, tomará desde el cero hasta ese número
    print(num)

# Forma no optima de recorrer una conjunto(No funciona en conjuntos)
for num in range(len(numeros)):
    print(numeros[num])

# Forma correcta de recorrer una conjunto
for num in enumerate(numeros):  # Enumate nos devuelve tuplas
    indice = num[0]
    valor = num[1]
    print(f'El indice es: {indice}, y el valor es: {valor}')

# Usando else/else
for num in numeros:
    print(f'Ejecutando el último bucle: {numeros}')
else:
    # Los else dentro de los for, se van a ejecutar siempre
    print("El bucle terminó.")

# Todo lo anteior funciona exactamente igual para tuplas, lista y conjuntos

# Probando
