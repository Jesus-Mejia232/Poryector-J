# Duración de otros cursos
cursos_min = 2.5
cursos_promd = 4
curso_max = 7
este_curso = 1.5

# Obteniendo el crudo de los cursos
crudo_curs_promd = 5
crudo_curs_actual = 3.5
# Obteniendo el porcentaje de diferencia entre los demás cursos
porcent_diferenciamin = 100 - este_curso / cursos_min * 100
porcent_diferenciamax = 100 - este_curso / curso_max * 10
porcent_diferenciapromd = 100 - este_curso / cursos_promd * 10
print("-----------------------------")
print("El curso de dalto dura un: ")
print(
    f" - Un: {round(porcent_diferenciamin,2)}% menos que el más rápido")
print(
    f" - Un: {round(porcent_diferenciamax,2)}% menos que el más lento")
print(
    f" - Un: {round(porcent_diferenciapromd,2)}% menos que el promedio")

# Calculando el porcentaje de tiempo vacío removido
vacio_eliminado_promd = 100 - cursos_promd / crudo_curs_promd * 100
vacio_eliminado_actual = 100 - este_curso / crudo_curs_actual * 100

print("-----------------------------")
print("El porcentaje de contenido vacío eliminado es de: ")
print(
    f" - Un: {round(vacio_eliminado_promd,2)}% del curso promedio")
print(
    f" - Un: {round(vacio_eliminado_actual,2)}% del curso de dalto")


# Mostrando diferencias si los cursos duraran 10 horas
print("-----------------------------")
print("Ver 10 horas de: ")
print(
    f" - De Dalto equivale a ver {round(cursos_promd / este_curso * 10 ,1 )} horas de un curso promedio")
print(
    f" - De un curso promedio equivale a ver {round(este_curso / cursos_promd * 100 ,1)} horas de un curso de dalto")
