# Funciones datos extra
# Estos parametros que tiene la funcion  "frase" Son parametros posicionales
def frase(nombre, apellido, adjetivo):
    return f"Hola {nombre} {apellido} sos demasiado {adjetivo}"


# Utilizando keyword arguments
# A poner el nombre del campo a donde ira ese dato, es forzar un argumento
frase_final = frase(apellido="Edgardo", adjetivo="Crack", nombre="Jesus")
print(frase_final)


# Cambiando los valores por defecto de los parametros
# Aquí estamos definiento un argumento por defecto
def frase2(nombre, apellido, adjetivo="inteligente"):
    return f"Hola {nombre} {apellido} pedazo de capo, sos demasiado {adjetivo}"


# Creando la misma opción con un parámetro opcional y un valor po defecto
# Aquí podemos cambiar los arguemntos que están por defecto en los parametros, tambien
frase_em_voz_alta = frase2("Jesus", "Edgardo", adjetivo="Fuerte")
# Se puede cambiar solamente poniendo el argumento, sin necesidad de "Invocar" al parámetro
print(frase_em_voz_alta)

#Esta es la función lambda aoisnaisodoasuduasiudausdus
