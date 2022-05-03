'''
miVariable = 3
print(miVariable)
miVariable = "abc def"
print(miVariable)
miVariable = 3.5
print(miVariable)
x = 10
y = 2
z = x + y
print(id(x))
# Las literales se escriben x088

a: str = 10.78  # En este caso la variable sigue siendo float, y el "str" es solo para una referencia para uno mismo o para otro programador que lea nuestro código.
print(type(a))  # Sirve para saber que tipo de variable es "a" si es string, int, float, etc.

b = False  # Variable tipo booleana (verdadero o falso). Se escribe con primer letra en Mayuscula.
print(type(b))

# Tipos int, float, String, Bool
x = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x = "Hola alumnos"
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))

# Manejo de cadenas (String)
miGrupoFavorito = "Pink Floyd: " + "The best Rock Band"

miGrupoFavorito2 = "Pink Floyd: "
caracteristicas = "The best Rock Band"
print("Mi grupo favorito es: ", miGrupoFavorito, caracteristicas)

# numero1 = "7"
# numero2 = "8"
# print(numero1 + numero2)
# print(int(numero1) + int(numero2))

# Tipos Booleanos (bool)
miBooleano = True
print(miBooleano)

miBooleano1 = 1 > 2
print(miBooleano1)

if miBooleano1:
    print("El resultado es Verdadero")
else:
    print("El resultado es Falso")

# Procesar la entrada del usuario
# funcion input (lectura de datos, pidiendolo, en esta funcion hacemos entrada y salida de datos)
# resultado = input("Digite un numero: ")  # Regresa un dato tipo String
# print(resultado)

# Conversion de la entrada de datos
numero1 = int(input("Escribe el primer numero: "))
numero2 = int(input("Escribe el segundo numero: "))
resultado = numero1 + numero2
print("El resultado de la suma es: ", resultado)


alto = int(input("Escriba el alto del rectangulo: "))
ancho = int(input("Escriba el ancho del rectangulo: "))
area = alto * ancho
perimetro = (alto + ancho) * 2
print("El area del rectangulo es ", area)
print(f"El perimetro del rectangulo es {perimetro} ")  #operador f interpolacion

miVariable3 = 10
print(miVariable3)

#Operadores de reasignacion
miVariable3 = miVariable3 + 1
print(miVariable3)

miVariable3 += 1    #Para sumar
print(miVariable3)

#miVariable3 = miVariable3 - 2
miVariable3 -= 2
print(miVariable3)

# miVariable3 = miVariable * 3
miVariable3 *= 3
print(miVariable3)

# miVariable3 = miVariable / 2
miVariable3 /=2
print(miVariable3)


#Operadores de comparacion

d = 4
b = 2
resultado = d == b #Comprobamos si son iguales
# resultado = 4 == 6 #Comprobamos si son iguales
print(resultado)

#Operador diferente

resultado = d != b
print(resultado)

#Operador mayor que

resultado = d > b
print(resultado)

#Operador menor que

resultado = d < b
print(resultado)

#Operador menor o igual
resultado = d <= b
print(resultado)

#Operador mayor o igual
resultado = d >= b
print(resultado)


numero = int(input("Ingrese un numero para saber si es par o impar: "))
print(f"El residuo de la division es: {numero % 2}")
if numero % 2 == 0:
    print(f"El valor del numero es: {numero} es un numero par")
else:
    print(f"El valor del numero es: {numero} es un numero impar")
'''

#Determinar si es mayor de edad
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print(f"Es mayor de edad, ya que su edad es {edad}")
    print("Es mayor de edad",edad)
else:
    print(f"Es menor de edad, usted tiene {edad}, y no puede tener esa bebida en la mano")

