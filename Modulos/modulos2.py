# Formas de invocar un modulo dentro de otro modulo
from modulo_saluda import saludar, saludar_raro
import modulo_saluda as saludo
# Con la funcion "as" podemos cambiar el nombre por el cual va a ser llamado el modulo, dentro del modulo donde se esta
# Invocando
saluda = saludo.saludar("Jesus")
print(saluda)

# Forma 2 de invocar un metodo, con esta forma podemos especificar que funcion, o funciones deseamos agregar a nuestro
# Nuevo modulo, para, de esta manera, no tener que estar poniendo el nombre del metod antes de la funcion requerida

saludar = saludar("Jesus")
saluda_raro2 = saludar_raro("Jesus")
print(saluda_raro2)
print(saludar)
