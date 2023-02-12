# Creando las listas

frutas = ["Manzana", "Pera", "Granada", "Durazno", "Mango", "Sandía"]
numeros = [1, 3, 4, 6, 8]

# Evitando que se coma una manzana con la sentencia "Continue"
for fruta in frutas:
    if fruta == "Mango":
        continue  # El "Continue" hace básicamente que el bucle salte ese elemento, y siga adelante con los demás elementos
    print(f"Me voy a comer una : {fruta}")

# Evitando que se coma un pera
for fruta in frutas:
    print(f"Me voy a comer una : {fruta}")
    if fruta == "Durazno":
        break
else:
    # El else no se ejecuta cuando hay un break
    print("Bucle terminado")

# For en una sola línea de código
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)


numeros_dup = [x*2 for x in numeros]
print(numeros_dup)
