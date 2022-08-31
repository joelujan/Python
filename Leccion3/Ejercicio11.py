'''
Ingresar "N" enteros, visualizar la suma de los numeros pares de la lista, cuantos numeros pares existen
y cuál es el promedio de los numeros impares
'''
num = int(input("Ingrese cantidad de numeros enteros a ingresar"))
i=1
sumapares = 0
sumaimpares = 0
conteopares = 0
conteoimpares = 0
while i <= num:
    ing = int(input(str(i)+", Ingrese numero: "))
    if (ing % 2 == 0):
        sumapares += ing
        conteopares += 1
    else:
        sumaimpares += ing
        conteoimpares += 1
    i += 1
print(f"La cantidad de numeros fue de: {num}, la cantidad de numeros pares es de {conteopares},su suma fue de {sumapares}, y la cantidad de impares fue de: {sumaimpares}, con la suma de {sumaimpares}")
