# Ejercicio 5 : Convertidor de temperaturas
# Realizar dos funciones para convertir de grados celsius
# a Fahrenheit y viceversa.
# Investigar la formula
def celsius_a_fahrenheit (celsius):
    return celsius * 9 / 5 + 32 #La precedencia de operacion : de izq a derecha.

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32 ) * 5 / 9 # Respetar la precedencia utilizando parentesis

celsius = float(input('Digite el valor de celsius: '))
resultado = celsius_a_fahrenheit(celsius);
print(f'Celsius {celsius} a F -> {resultado:.2f} Fahrenheit') # esto es para q muestre solo 2 resultados despues de la coma
fahrenheit = float(input('Digite el valor de fahrenheit: '))
resultado = fahrenheit_a_celsius(fahrenheit)
print(f'Fahrenheit {fahrenheit} a C -> {resultado:.2f}')