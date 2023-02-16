"""# Si el modulo estubiera dentro de una carpeta en la misma ruta:
# import funciones_buenas.saludar as m_saludar

import saludar as modulo_saludar
import sys

sys.path.append("C:\\Projectos J\\Poryector-J\\Funciones_buenas")

print(modulo_saludar.hola("Jesus"))
# "dir" Me muestra todas las propiedades y metodos que ese elementos tenga

# Para ver las propiedades y métodos del namespace:
# print(dir(modulo_saludar))
print(__name__)  # Accedemos al nombre de este modulo
# print(modulo_saludar.__name__) #Accediendo al nombre del modulo llamado
"""
