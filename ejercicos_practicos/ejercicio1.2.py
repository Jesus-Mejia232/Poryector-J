frase = input("Digite una frase : ")
frase_separada = frase.split(" ")
cantidad_palabras = len(frase_separada)
total_tiempo = cantidad_palabras/2
print(
    F"Dijiste {cantidad_palabras} palabras, y tardarías {total_tiempo} segundos en decirlo")

print(f"Dalto tardaría en decirlo {total_tiempo * 100 // 2 * 1.3 / 100}")

if (cantidad_palabras >= 120):
    pritnt("Para flaco, no te pedí un testamento")
