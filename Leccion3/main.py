#Ciclo While
condicion = True
while condicion:
    print('Ejecutando el ciclo While')
else:
    print('Fin del ciclo While')

#Otro ejemplo
contador = 0
while contador < 4:
    print(f'Ejecutamos nuestro ciclo while {contador}')
    contador += 1
else:
    print('Fin del ciclo while')

#Ejercicio: imprimir numeros de 0 al 5 con el ciclo while
maximo = 5
contador = 0
while contador <= maximo:
    print(contador)
    contador += 1

#Ejercicio : imprimir numeros del 5 al 1 de manera descendente
minimo = 1
contador = 5
while contador >= minimo:
    print(contador)
    contador -= 1

#Ciclo For
cadena = 'Hello'
for letra in cadena: #in es por indice
    print(letra)
else:
    print('Fin del ciclo for')

#Palabra reservada break
for letra in 'Alemania':
    if letra == 'a':
        print(f'Letra encontrada: {letra}')
        break #rompe la estructura y termina
else:
    print('Fin del ciclo for')

#Palabra reservada continue
for i in range(6):
    if i % 2 == 0:
        print(f'Valor: {i}')

for i in range(6):
    if i % 2 != 0:
        continue #Eludir o anular todos los numeros q son impares
        print(f'Valor: {i}')


