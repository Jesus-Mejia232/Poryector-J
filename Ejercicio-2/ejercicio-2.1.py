# Hoy falto el profesor de clase y los alumnos planificaron hacer la suya propia
# 1 alumno va a ser el profesor
# 1 alumno va a ser el asistente

"""Pedir los datos de los alumnos que vinieron hoy a clase y ordenar los datos de mayor a menor

El mauyor de la clase es el profesor y el menor es el asistente. Quien es quien?"""

# Diargama de flujo:

# Pedir el nombre y edad
# Ver cual es mayor
# Ver cual es menor


def obtener_compañeros(cantidad_compañeros):
    compañeros = []
    for i in range(cantidad_compañeros):
        nombre = input("ingrese el nombre del compañero: ")
        edad = int(input("Ingrese la edad del compañero: "))
        compañero = (nombre, edad)
        compañeros.append(compañero)

    # "Key" dentro de la funcion lambda sirve para decirle al programa que nos muestre
    # Ordenando de menor a mayor según su edad,
    compañeros.sort(key=lambda x: x[1])
    # El segundo valor de la tupla,lista o diccionario, NOTA: Debe ser capáz de tomar un elemento del objeto que está siendo
    # Ordenado y devolver un valor que pueda ser comparado con otros elementos.
    # Esto porque en la lista los elemntos están de la siguiente manera "[(1,2),(1,2),(1,2)]"
    asistente = compañeros[0][0]
    # Accede al grupo del parentesís, número 1, al elemento 1, al poner su indice
    profesor = compañeros[-1][0]
    # Estos dos nombres solo existen, dentro de la función (obtener_compañeros)
    return asistente, profesor


# Este es un desempaquetado de elementos
asistente, profesor = obtener_compañeros(5)
print(f"El profesor es: {profesor} y el asistente es: {asistente}")

# Recuerda siempre hacer el commit y el push, luego de crear cambios
# El comando es "git commit -m "Esto es un ejemplo" (solamente poner las comillas que hay dentro del ejemplo)"
# Las comillas de afuera no se ponen, para que la terminal lea correctamente el comando
