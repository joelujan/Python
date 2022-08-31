'''Dadas las horas trabajadas de 5 personas y la tarifa de pago. Calcular el salario, y la sumatoria de todos los salarios'''
'''
suma = 0
i = 1
while i<=5:

    horas = int(input("Ingrese la cantidad de horas trabajadas del trabajador:"+str(i)+" :"))
    precio = int(input("Ingrese el salario por hora: "))
    salario = horas * precio
    suma += salario
    print(f"El salario de la persona {i}, es de: {salario}")
    salario = 0
    i += 1
print(f"La suma de todos los salarios es: {suma}")
'''
suma = 0
for i in range(1,6):
    horas = int(input("Ingrese la cantidad de horas trabajadas del trabajador:"+str(i)+" :"))
    precio = int(input("Ingrese el salario por hora: "))
    salario = horas * precio
    suma += salario
    print(f"El salario de la persona {i}, es de: {salario}")
    salario = 0
print(f"La suma de todos los salarios es: {suma}")