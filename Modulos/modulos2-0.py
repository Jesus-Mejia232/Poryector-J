# Si el modulo estubiera dentro de una carpeta en la misma ruta:
# import funciones_buenas.saludar as m_saludar

import saludar as modulo_saludar
import sys

sys.path.append("C:\\Projectos J\\Poryector-J\\Funciones_buenas")

print(modulo_saludar.hola("Jesus"))
