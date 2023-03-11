import re

texto = """Siempre. creando una cadena de texto, esto es simplente un ejemplo, para poder crear (1 linea) 
Esta es la siguiente linea de texto de la cadena 2256565 linea 
Esta es la tercer linea(3 linea) de texto 5151 25 51451que ya Está lista     """

# Haciendo la parte simple
# resultado = re.search("Esta", texto, flags=re.IGNORECASE) "flags=re.IGNORECASE" sirve para decirle a la funcion que
# Ignore todas las mayusculas y minsuculas


# Más funciones:
# \d --> sirve para buscar digitos numericos del 0 - 9
# Si ponemos la "D" Mayuscula, el lugar de la minuscula, buscará todo lo contrario. Es decir, buscará todos
# Datos que no sean numericos
# le estamos diciendo que busque todos los digitos numericos, del 1 al 9
# esultado = re.findall(r"\D", texto)

# \w si usamos la w buscará todos los datos alfa numericos
# Datos alfanumericos, tales como (de la  "a-z", "A-Z","0-9","_")
# resultado = re.findall(r"\w", texto)
# Si usamos la "W" mayuscula buscará todo lo contrario

# \s la "s" busca espacios en blanco --> espacios, tabs, saltos de linea
# la "S" mayuscula nos devuelve, todo menos espacios, tabs, saltos de linea
# resultado = re.findall(r"\S", texto)

# El "." busca TODO menos saltos en linea
resultado = re.findall(r".", texto)

# "\n" para buscar saltos
resultado = re.findall(r"\n", texto)

# "\" Cancela todos los caracteres especiales
# Cancelando la funcion del punto, y buscando puntos
resultado = re.findall(r"\.", texto)


# Armando una cadena que busque un numero, seguido de un punto y un espacio
# Solamente arrojará en consola la cadena que coinsida con el patron que le
resultado = re.findall(r"\d\.\s", texto)
# Pasamos, si no encuentra ninguna, no imprimirá nada

# "^" sirve para buscar el comienzo de una liena (Su nombre es acendo circunflejo)
# El "flags=re.M" sirve para decirle que queremos que la bsucaqueda sea multilinea
# Buscando una palabra al principio de la linea
resultado = re.findall(r"^Siempre", texto, flags=re.M | re.I)

# "$" Busca el final de una linea
resultado = re.findall(r"$lista", texto, flags=re.M)

# {n} -> busca n cantidad de veces el valor de la izquierda
# Con esto le estamos diciendo al programa que busque(en este caso), 3 numeros
# Juntos
resultado = re.findall(r"\d{3}", texto)

# Tenemos para buscara por rangos, tenemos para mostrar Como menos "n" cantidad de veces, y como maximo "m" cantidad
# De veces "{n,m}"
# Traduciendo esto, le estamos pidiendo que nos busque todos los datos en los que,
resultado = re.findall(r"\d{1,4}", texto)
# Hayan, 1, 2 , 3 o 4 numeros juntos

# "|" Busca una cosa o la otra
resultado = re.findall(r"\d{2,4} | hola", texto)
print(resultado)
# DATO importante: comentar las lienas de codigo innecesarias ayuda a que el programa sea más rapido
