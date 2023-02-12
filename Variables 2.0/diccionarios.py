# Creando un diccionario

# Creando diccionarion con Dict()

# NOTA IMPORTANTE:Si queremos crear diccionarios vacíos, necesitamos
diccionario = dict(nombre="Jesus", apellido="Mejia", edad="16")
# Usar la función "Dict()"

# Las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["Jesus", "Mejia un crack"]): "Así es jajajajja"}

# Creando diccionario con fromkeys
# Para que los valores de cada elemento se imrpriman en none, la función
# debe que llevar "[]"
diccionario = dict.fromkeys(["Nombre", "Jesus"])

# Creando dicionario con fromkeys sin las "[]"
# Asigna el valor 2 a cada letra del valor 1
diccionario = dict.fromkeys("ABCDE", "Jesus")

# Cambiando el valor por defecto a "No se"
diccionario = dict.fromkeys(["Nombre = "], "No sé")

print(diccionario)
