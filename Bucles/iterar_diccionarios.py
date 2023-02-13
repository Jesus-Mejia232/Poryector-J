diccionario = {
    "Nombre": "Jesus",
    "Apellido": "Edgardo",
    "Edad": 16
}

# El key en está función, puede ser cualquier nombre
for key in diccionario.items():  # Con el punto item se puede iterar el diccionario
    key  # Esta es un método único para iterar claves
    print(f"La clave es: {key}")


for datos in diccionario.items():  # Con el punto item se puede iterar el diccionario
    clave = datos[0]
    valor = datos[1]
    print(f"La clave es: {clave}, y el valor es: {valor}")
# Probando
