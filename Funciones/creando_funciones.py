"""# Creando función simple

def saludar():
    print("Que tal Jesus como estás")


saludar()
"""

# Creando una funcion que tenga parametros


def saludar(nombre, sexo):
    sexo = sexo.lower()
    if (sexo == "hombre"):
        adjetivo = "maquina"
    elif (sexo == "mujer"):
        adjetivo = "objeto"
    else:
        adjetivo = "amor"

    print(f"Hola {nombre} como estás {adjetivo}, como va todo?")


saludar("Jesus", "Hombre")
saludar("Lobo", "No lo se")
saludar("Maria", "Mujer")

# Crenado una función que retorne valores


def calculo(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num * 2}"
    return contraseña, num  # Esto ya es una tupla, por la coma


# Desenpaquetando
password, num = calculo(4)
print(f"Tu nueva contraseña e: {password}")
print(f"Tu contraseña fue creada con el número: {num}")
