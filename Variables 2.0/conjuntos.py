# Crenado un conjunto con set
conjunto = set(["Jesus", "Edgardo", "Mejia", 16])

# Metiendo un conjunto dentro de otro conjunto
# El frozenset sirve para congelar un conjunto, se puede usar
conjunto1 = frozenset(["Dato1", "jesus", "edgardo", "Mejia"])
# para meter ese conjunto dentro de otro conjunto
conjunto2 = {conjunto1, "dato3_de_conjunto"}

print(conjunto2)


#                                    """Teoría de conjuntos"""

conjunto3 = {1, 2, 3, 4, 5, 6}
conjunto4 = {1, 3, 2}

# Verificando si es un subconjunto
comparacion = conjunto4.issubset(conjunto3)
comparacion = conjunto4 <= conjunto3

# Verificando si es un super conjunto
comparacion = conjunto4.issuperset(conjunto3)
# A difencia de el subconjunto con la comparación del super conjunto solo se poner el
comparacion = conjunto4 > conjunto3
# un operador de compración

# Verificar si hay algún número en común
# Devuelve true cuando los conjuntos que se están comparando hay siquiera un
comparacion = conjunto4.isdisjoint(conjunto3)
# Elemento distinto

print(comparacion)

# Verificando si es un sub conjunto

comparacion = conjunto1.issubset(conjunto2)

print(comparacion)
