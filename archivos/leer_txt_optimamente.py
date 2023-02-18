# Esta manera es lo mismo, pero mucho más óptimo que en la forma anterior(Se refiere a la manera de leer del archivo
# "leer.txt")

# Abriendo el archivo con with open
with open("archivos\\Jesus.txt", encoding="UTF-8") as archivo:
    # Leemos el archiivo
    contenido = archivo.read()

    # Mostramos el archivo
    print(contenido)

# No es necesario cerrarlo al usar el with open
