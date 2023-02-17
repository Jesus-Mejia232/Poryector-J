# Con "as" se cambia el nombre predeterminado del modulo, NOTE el nuevo nombre
import funcion_buenas.saludar as m_saludar
# Modificado solo funciona en el modulo actual, con esto se simplifica el nombre en casos en los que el namespace
# Del modulo sea demasiado largo y tedioso de escribir

print(m_saludar.saludar("Jesus"))
