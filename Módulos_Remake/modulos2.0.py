# Con "as" se cambia el nombre predeterminado del modulo, NOTE el nuevo nombre
# import funcion_buenas.saludar as m_saludar
# Modificado solo funciona en el modulo actual, con esto se simplifica el nombre en casos en los que el namespace
# Del modulo sea demasiado largo y tedioso de escribir


# Para importar las funciones de un modulo fuera de la carpeta es de la siguiente manera:

# import saludar
# import sys

# sys.builtin_module_names NOTE Nos devuelve una tupla con todos los valores de las propiedades, similar a "dir"

# sys.path.append("C:\\Projectos J\\Poryector-J\\funciones_buenas")
# rint(sys.path)


# print(saludar("jesus"))


# .:Dato:. si mi modulo tiene el mismo nombre que una funcion integrada de python, cuando importe mi modulo
# Python jalara la funcion integrada, no mi modulo, esto es porque python le da prioridad a los modulos integrados
