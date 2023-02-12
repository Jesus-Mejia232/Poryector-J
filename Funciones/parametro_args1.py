# Forma no optima sumar

def sum1(lista):
    numeros_sumados = 0
    for numero1 in lista:
        numeros_sumados = numeros_sumados + numero1
    return numeros_sumados


resultado_sum1 = sum1([1, 24])
print(resultado_sum1)

# Forma correcta de sumar, copiando de cierto modo a la anterior


def sum2(numero2):
    # NOTA: Crear la variable a lista, para que pueda ejecutarse
    return sum([*numero2])


reultado_sum2 = sum2([23, 4, 5, 6, 7, 77])
print(reultado_sum2)

# Forma definitiva de sumar, usando el operador * como argumento (*args)


def sum3(nombre, *numero3):  # NOTA: De está forma nos limitamos a que siempre tiene que ser el último parámetro que agreguemos
    return f"{nombre}, la suma de tus números es: {sum(numero3)}"


resultado_sum3 = sum3("Jesus", 21, 3)
print(resultado_sum3)
