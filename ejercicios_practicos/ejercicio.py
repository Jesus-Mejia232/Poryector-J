"""Diferencia de porcentaje entre el curso actual y:
El más rápido de otros cursos Actual = 1.5
Más rápido = 2.5
El más lento de otros cursos = 7
El promedio de los cursos = 4
"""

actual = 1.5
mas_rap = 2.5
promed = 4
mas_lent = 7

"""__________________________________A)_______________________________________"""


#Obteniendo el porcentaje de diferencia entre el curso más rápido y el actual

porcent_rap = int((actual / mas_rap) * 100) - 100

print(f"EL porcentaje de diferencia que hay entre el curso más rápido y el actual es de: {porcent_rap}%")

#Obteniendo el porcentaje de diferencia entre el curso más lento y el actual
porcent_lent = int((actual / mas_lent) * 100) - 100

print(f"EL porcentaje de diferencia que hay entre el curso más lento y el actual es de: {porcent_lent}%")

#Obteniendo el porcentaje de diferencia entre el curso promedio y el curso actual

porcent_promed = int((actual / promed) * 100) - 100

print(f"EL porcentaje de diferencia que hay entre el curso promedio y el actual es de: {porcent_promed}%")

print("   ")
print("                              __B)__  ")


"""__________________________________B)___________________________________________"""

crudoactu = 3.5
crudopromd = 5

#Obteniendo el porcentaje de diferencia entre el curso más rápido y el actual

porcent_rap = int((actual / crudoactu) * 100) - 100

print(f"EL porcentaje de crudo eliminado en el curso actual es de : {porcent_rap}%")

#Obteniendo el porcentaje de diferencia entre el curso promedio y el curso actual

porcent_promed = 100 - actual / crudopromd * 100

print(f"EL porcentaje de crudo elminado de los cursos promedio es de : {porcent_promed}%")

"""__________________________________C)___________________________________________"""

    