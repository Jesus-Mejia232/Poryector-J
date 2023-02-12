"""Qué es un método? 

Los metodos son funciones aplicadas a objetos

Los metodos analizan pedazos de códigos que el usuario les da, para devolvernos o hacer
cosas con ellos """

cadena1 = "asbnduiasd44545a"
cadena2 = "Bienvenido Usuario nuevo"

# Convierte a Mayúsculas

mayusc = cadena1.upper

# Convierte a minusculas

minusc = cadena2.lower

# Primera letra mayuscula
primer_mayusc = cadena1.capitalize()

# Buscamos la un valor dentro de una cadena, si no hay coincidencias, devuelve -1

busqueda_find = cadena1.find("d")

print(busqueda_find)

# Si no encuentra una coincidencia lanza una excepcion

busqueda_index = cadena1.index("s")

print(f"El resultado de index es:{busqueda_index}")

# Si es numerico devuelve true, sino, devuelve false

es_numerico = cadena1.isnumeric()

print(es_numerico)

# Si es alfanumerico devuelve true, sino, devuelve false

es_alfanumerico = cadena1.isalpha()

print(es_alfanumerico)

# Contamos las coincidencias de una cadena, dentro de otra cadena, devuelve la cantidad de
# Coincidencias
contar_coincidencias = cadena1.count("a")

print(contar_coincidencias)


# Funcion "Len" Contramos cuantos caracteres tiene una cadena

contar_caracteres = len(cadena1)

print(contar_caracteres)


#Verificamos si una cadena empieza con una determinada cadena, si es así, nos devuelve True

empieza_con = cadena1.startswith("as")

print(empieza_con)


#Verificamos si una cadena termina con una determinada cadena, si es así, nos devuelve True

termina_con = cadena1.endswith("a")

print(termina_con)

#Si el valor 1 lo encuentra en la cadena original, remplaza el valor 1 de la mismas, por el valor 2 
cadena_nueva = cadena1.replace("asbnduiasd44545a", "Esta,Es UNA NUEVA CADENA,A base de la,antigua cadena")
cadena_nueva2 = cadena_nueva.capitalize()
print(cadena_nueva2)

#Split, separa cadenas con la cadena que le demos. NOTA: nos devuelve un tipo de dato lista

cadena_separada = cadena_nueva2.split(",") #Crea una lista, en la cual busca el dato que le pasamos y por cada vez
                                     #Que enuentre ese dato, agregará un espacio a la cadena

print(cadena_separada[3])


#Buscando si un elemento se encuentra en la lista NOTA: En las listas o tuplas, el metodo index
#Busca el indice donde se encuentra el elemento buscado, en cambio en las cadenas, devuelve 
#La cantidad de coincidencias que tiene ese elemento en dicha cadena<