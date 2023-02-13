# Creando una lista con list(Más que todo se usa para crear listas vacías luego usarlas)

lista = list([53, 59, 52, 700, 70, 500])

# Devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)


# Agregando elementos a lista con append

lista.append(55)

# Agregando elementos a la lista con insert(Con insert agregamos elementos en el indice que indiquemos)
# Se pone primero le indice en el que se quiere agregar el elemento y luego el elemento, pero no elimina
# El elemento anterior en ese indice, sino que lo manda a un indice posterior al del este

lista.insert(2, 40)

# Agregando elementos a la lista con extend(Este metodo nos permite agregar varios elementos de un solo
# a la lista)

lista.extend([62, 80])

# Eliminando elementos de la lista con pop(ingresando el valor de indice que se quiere eliminar)
# -1 para eliminar el ultimo, -2 para eliminar el antepenultimo, y así sucesivamente
lista.pop(0)

# Removiendo un elemento por su valor, si lo encuentra, lo elimimna
lista.remove(55)

# Clear, elimina todos los elementos de la lista
# lista.clear()


# Ordenando la lista de fomra ascendente (si usammos el parámetro reverse=True, lo ordena en reversa)

lista.sort()

# Invirtiendo el orden de la lista, basando en el orden actual
lista.reverse
print(lista)

# Buscando si un elemento se encuentra en la lista NOTA: En las listas o tuplas, el metodo index
# Busca el indice donde se encuentra el elemento buscado, en cambio en las cadenas, devuelve
# La cantidad de coincidencias que tiene ese elemento en dicha cadena<
elemento_encontrado = lista.index(80)

print(elemento_encontrado)
