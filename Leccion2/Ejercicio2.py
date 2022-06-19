'''
# Ejercicio 2:
# Determinar la solución lógica de la siguiente operación.
a = float(input("Digite a: "))
b = float(input("Digite b: "))

resultado = ((3 + 5 * 8) and ((-6 / 3 * 4) + 2 <2)) or (a > b)
print("El resultado es:", resultado)

# Ejercicio 3:
# Intercambiar el valor de dos variables.

a = float(input("Digite el valor de a: "))
b = float(input("Digite el valor de b: "))

c = a
a = b
b = c

print("El nuevo resultado de a es:", a , "el nuevo resultado de b es:", b )

import math
# Ejercicio 4:
# Hacer un programa para ingresar el radio de un circulo
# y se reporte su área y la longitud de la circunferencia.

# Área = Pi * r2
# Longitud = 2 * Pi * r

r = float(input("Digite el radio de la circunferencia: "))

p = math.pi
area = p * r ** 2
longitud = 2 * p * r
print("El area es:", area, ". La longitud es:", longitud)
'''