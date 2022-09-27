# Ejercicio 01: Crear una funcion para sumar los valores recibidos de tipo
# numéricos, utilizando argumentos variables *args como parámetro de la
# función y agregar como resultado la suma de todos los valores pasados
# como argumentos.
# definimos una función
def sumar_valor(*args):  # Recibimos una cantidad de parámetros indefinidos
    resultado = 0
    #iteramos cada elemento
    for valor in args:
        resultado += valor
    return resultado

    # pass   para no dejar vacia la función y no largue error



# llamamos a la función
print(sumar_valor(3, 5, 9))
