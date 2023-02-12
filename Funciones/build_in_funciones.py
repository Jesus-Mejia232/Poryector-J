numeros = [2, 6, 5.6]

# Encontrando el número más alto
numero_más_alto = max(numeros)
print(numero_más_alto)

# Encontrando el número menor
numero_menor = min(numeros)
print(numero_menor)


# Redondeando decimales
# La función "Round" sirve para, como su nombre indica, redondear. El segundo valor que se ingresa
numero = round(12.345345, 2)
# Es para indicar cuántods carácteres se quieren poner después del punto decimal
print(numero)

# Retorna False : vacío,0,False,None. Devolvera Verdadero, cuando: True, un número distinto de 0, Cadena  o datos no vacíos
numero_bool = bool(2)
print(numero_bool)

# Devuelve true solo si todos los elementos son verdaderos
resultado_all = all(["Jesus", 0, "Para ganar", "Edgardo"])
print(f"El resultado booleano es: {resultado_all}")

# Sumando los elementos
sumando = sum(numeros)
print(sumando)  # Devuve una excepcion si la lista contiene distintos a float o int
