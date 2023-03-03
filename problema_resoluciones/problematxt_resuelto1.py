#Tenemos dos listas con nombre y apellido, es decir una con nombres y otra con apellidos
#Tenemos que escribir los datos de forma óptima, en un archivo de texto con un for

nombres = ["Jesus","Edgardo","Marco","Hector","Lucas"]
apellidos = ["Mejia","Acosta","Perez","Lagos","Dalto"]

with open("problema_resoluciones//ejercicio_listo","w") as archivo:
    archivo.writelines("Los datos son:\n\n")
    for n,a in zip(nombres,apellidos):
        archivo.writelines(f"Nombre:{n}\n")
        archivo.writelines(f"Apellido:{a}\n-----------\n")


#Si queremos crear el for en una sola línea de código es de la siguiente manera:
#Basicamente se pone lo que va en la segunda linea de codigo del for, antes de el, y todo eso, dentro de 
#Una lista
#[archivo.writelines(f"Nombre:{n}\nApellido:{a}") for a,n in zip(nombres,apellidos)]