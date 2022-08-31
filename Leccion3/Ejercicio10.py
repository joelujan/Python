'''
//Calcular el factorial de un numero mayor o igual a 0(Diagrama de flujo)
num = int(input("Ingrese el numero que desea calcular el factorial"))
factorial = 1
i= 1
while i<= num:

    factorial = i * factorial
    i = i + 1
print(factorial)
'''

num = int(input("Ingrese el numero que desea calcular el factorial"))
if num<0:
    print("El factorial de 0, o algún numero negativo no se puede calcular")
else:
    i = 1
    factorial = 1
    while i <= num:
        factorial *= i
        i += 1
    print(f"El factorial de :{num}, es {factorial}")
