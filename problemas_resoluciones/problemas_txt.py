# Escribir los datos de dos litas de forma optima en un for:

nombres = ["Jesus", "Edgardo", "Marco", "Tulio"]
apellidos = ["Mejia", "Acosta", "Perez", "Bueso"]


with open("problemas_resoluciones\\problema1_resuelto", "w") as archivo:
    archivo.writelines("Los datos son: \n\n")
    for n, a in zip(nombres, apellidos):
        archivo.writelines(f"Nombre : {n}\nApellido {a}\n-----------------\n")

# Leyendo los datos de forma optima, con un for:
