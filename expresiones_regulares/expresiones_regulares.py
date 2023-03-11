import re

texto = """Siempre creando una cadena de texto, esto es simplente un ejemplo, para poder crear (1 linea) 
Esta es la siguiente linea de texto de la cadena(2 linea) 
Esta es la tercer linea(3 linea) de texto que ya Está lista"""

# Haciendo la parte simple
# resultado = re.search("Esta", texto)

# Más funciones:
# \d --> sirve para buscar digitos numericos del 0 - 9
# Si ponemos la "D" Mayuscula, el lugar de la minuscula, buscará todo lo contrario. Es decir, buscará todos
# Datos que no sean numericos
# le estamos diciendo que busque todos los digitos numericos, del 1 al 9
resultado = re.findall(r"\D", texto)

# \w si usamos la w buscará todos los datos alfa numericos
# Datos alfanumericos, tales como (de la  "a-z", "A-Z","0-9" "_")
resultado = re.findall(r"\w", texto)
# Si usamos la "W" mayuscula buscará todo lo contrario

# \s la "s" busca espacios en blanco --> espacios, tabs, saltos de linea
# la "S" mayuscula nos devuelve, todo menos espacios, tabs, saltos de linea
resultado = re.findall(r"\S", texto)


print(resultado)
# DATO importante: comentar las lienas de codigo innecesarias ayuda a que el programa sea más rapido
