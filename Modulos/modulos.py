# Formas de invocar un modulo dentro de otro modulo
# El lugar donde va el nombre del modulo, se le llama "namespace", para importar
#            from Funciones_buenas.saludar import saludar, saludar_raro
# Todas las funciones y no tener que andar poniendo el nombre del modulo, para jalar todas las funciones se pone un *
# Pero es una pesima practica de programacion
# Con el "as" le podemos cambiar el nombre a funciones especificas
# Así se importa un modulo que esta dentro de otra carpeta
#         import Funciones_buenas.saludar as saludo
# Con la funcion "as" podemos cambiar el nombre por el cual va a ser llamado el modulo, dentro del modulo donde se esta
# Invocando
#      saluda = saludo.saludar("Jesus")
#         print(saluda)

# Forma 2 de invocar un metodo, con esta forma podemos especificar que funcion, o funciones deseamos agregar a nuestro
# Nuevo modulo, para, de esta manera, no tener que estar poniendo el nombre del metod antes de la funcion requerida

#    saludar = saludar("Jesus")
#     saluda_raro2 = saludar_raro("Jesus")
#     rint(saluda_raro2)
#     print(saludar)

# La formas de acceder a un modulo dentro de una carpeta es la siguiente
# "nombre_de_la_carpeta.modulo_saludar" De esta manera podemos acceder a al modulo y por enede a al funcion
