# Ejercicio 2: Función con * args para multiplicar
# crear una función para multiplicar los valores recibidos
# de tipo numérico, utilizando argumentos variables *args
# como parámetro de la funcion y regresar como resultado
# la multiplicación de todos los valores pasados como argumentos
def multiplicar(*args): #El mas utilizado es *arg
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado


#Llamamos a la función
print(multiplicar(3, 5, 15, 3)) #Le pasamos los argumentos
