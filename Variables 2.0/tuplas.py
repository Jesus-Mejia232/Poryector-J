#Creando la tupla

tupla = tuple(["Jesus","Edgardo","Mejía","Acosta"])#NOTA: Poner las "[]" al crear la tupla con la función "tuple"
#Si no no se creará

#Otra forma es crear una tupla con multiples datos, sin parentesís 
tupla = "Jesus","Mejia"

#Creando una tupla sin parentesís con un solo dato NOTA: Poner una coma al final, para que python detecte que es 
# una tupla y no un tipo de dato string, común y corriente: #NOTA: Cuando se ponen multiples datos, no hace falta 
# poner una coma al final:
tupla = "Jesus",

print(tupla)

"""La tuplas la debemos crear cuando son datos de solo lectura"""

"""La razón por la cual las tuplas son modificables es porque crean dos espacios de memoria, y uno lo van modificando
y luego de modificar uno modifican el otro(En bucle), es por esa razón que las listas son mutables. En cambio las
tuplas solo tinen un espacio de memoria, y por ello son inmutables
"""
