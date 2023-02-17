# Esta es una forma de llamar a un método para usar sus funciones y cambiando el nombre a "m_saludar"
# import "name_de_modulo(namespace se llama el campo)" "name de la función" as(con "as" se asigna un nuevo nombre a la funcion
# o al modulo en sud efecto) NOTE Esto claro, solo se hace si el modulo con las funciones que necesitmaos está
# en otra carpeta que no es la misma que en la que estamos, evitentemente

# si vamos a acceder al modulo que está en la misma carpeta, lo hacemos de la siguiente manera
import modulo_saludar

# Si solo queremos importar la función, podemos usar lo siguiente
# from modulo_saludar import saludar #La ventaja de usar este metodo es que ya no es necesario llamar al namespace a la hora
# De usar la función

# Cuando los modulos son llamados, sus funciones pasan de ser llamdas funciones a ser metodos
# Esto porque toca poner le punto despues del nombre del modulo, como si se tratase de un metodo como los demas

# Para acceder al nombre del modulo que imporamos usamos el parámetro "__name__"
"""saludo = (modulo_saludar.__name__)
print(saludo)"""
