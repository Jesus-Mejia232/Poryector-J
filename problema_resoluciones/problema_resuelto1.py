#Tenemos dos listas con nombre y apellido, una con nombre y otra con apellido, tenemos que escribir 
#Los datos de forma optima, en un archivo de texto con un for

nombres = ["Jesus","Edgardo","Marco","Hector","Maria"]
apellidos = ["Mejia","Acosta","Perez","Rivera","Lagos"]

with open("problema_resoluciones//resolucion","w") as archivo:
    archivo.writelines("Los datos son:\n---------------\n")
    for n,a in zip(nombres,apellidos):
        archivo.writelines(f"Nombre: {n}\n")
        archivo.writelines(f"Apellido: {a}\n-----------------\n")