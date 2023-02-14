# Crear una funcion que al darle un numero genere numeros primos hasta llegar a ese numero

#Creando la función que verifique si un número es primo
def es_primo(num):
    #Verificamos que el numero pasado no pueda dividirse por 2, y ese mismo numero 
    for i in range(2,num):
        if num%i==0: return False #Si es divisible por alguno retornamos False y hasta aquí termina el bucle
    return True #Si el bucle llega hasta aquí significa que el divisible, entonces devolvemos True 

#Creamos la funcion de nos devuelva todos los número primos hasta el número que pongamos 
def primos_hasta(num):
    #Creamos la lista
    primos = []
    for i in range(num+1):
        #Verificamos si el valor es primo
        resultado = es_primo(i)
        #En caso de que lo sea, lo agregamos a la lista
        if resultado == True: primos.append(i)
    #Devolvemos la lista
    return primos 

resultado = primos_hasta(98)
print(resultado)