# Comenzamos con funciones
# Definimos una función
def mi_funcion(): #Snake case Usamos esto para identificar a la función utilizamos paréntesis
    print('Saludos a todos los alumnos de la Tecnicatura')

mi_funcion() #Estamos llamando a la función, se puede llamar n veces. No se puede llamar antes
#de definir una función.
mi_funcion() #Se puede llamar a una funcion N cantidad de veces


# Desempaquetado de listas o list Unpacking

def show(name, lastName):
    print(name+' '+lastName)
person = ["Ariel", "Betancud"] #Desempaquetamos con una lista
show(person[0],person[1]) #Pasamos uno por uno los datos de la lista a la funcion
show(*person) #Esto es lo mismo que lo anterior pero le pasamos todo junto
person2 = ("Osvaldo", "Giordanini") #Desempaquetamos a través de una tupla (Es tupla por los parentesis)
show(*person2)
person3 = {"lastName" : "Lucero", "name": "Natalia"} #Desempaquetamos a través de un diccionario
show(**person3) #Acá ocupamos ** por q es llave,valor
#Repaso for else
numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n)
#    if n == 3:
#        break #Esta es la unica manera para que no se ejecute el else
else:#el else siempre se ejecuta a menos que exista un break
    print('Esto se terminó')

# List comprehension, lista de compresion
names = ["Paolo", "Rodrigo", "Lupe", "Pepe"]
alongP = [p for p in names if p[0] == 'P']#compresion, tomar lo necesario de esta lista, creando una lista nueva
#p para cada elemento, de p, in names q es la lista, luego una condicion que desde 0 en adelante es igual su primer letra[0],
#= a P se va a guardar en una nueva lista alonP
print(alongP)
bottleC = [{"name": "Quilmes", "country": "Arg"},
           {"name": "Corona", "country": "Mx"},
           {"name": "Stella Artois", "country": "Belgium"}]
Arg = [b for b in bottleC if b["country"] == "Arg"]#mismo ejemplo de comprehension, pero con diccionario
print(Arg)
print(bottleC)

# Paso de argumentos(funciones)


def mi_funcion2(name, lastName): # Parámetros son las variables q declaremos en la funcion
    print("Saludos a todos los que ven la clase a través del canal de You Tube")
    print(f'Nombre: {name}, Apellido: {lastName}')


mi_funcion2('Jorge', 'Lucero') # Argumentos es el valor que enviamos a la función
mi_funcion2('Ariel', 'Betancud')
mi_funcion2('Analia', 'Pedrosa')


# La palabra return en funciones
# Creamos una función para sumar
def sumar(a, b):
    return a + b


# resultado = sumar(78, 22)
# print(f'El resultado de la suma es: {resultado}')              Dos formas de hacer lo mismo para llamar a funciones
print(f'El resultado de la suma es: {sumar(55, 45)}')


def sumar2(a:int = 0, b:int = 0) -> int:  #Valor por default para que no haya error. por las dudas si se olvida de pasar un argumento
#def sumar2(a:int = 0, b:int = 0) -> int:  #Valor por default para que no haya error. Aca hacemos redundancia
    return a + b
resultado = sumar2()
print(f'Resultado de la suma: {resultado}')
print(f'Resultado de la suma: {sumar2(22, 66)}')

# Argumentos, variables en funciones


def listarNombres(*nombres):  # Parametro: *nombres o *args para que varien los argumentos porque desconocemos la entrada
    for nombre in nombres: # Se va a convertir en una tupla, xq no pueden ser modificadas
        print(nombre)
listarNombres('Lucas', 'José', 'Claudia', 'Rosa', 'María') #Argumentos
listarNombres('Marcos', 'Daniel', 'Romina', 'Pepe', 'Marcela', 'Carlos')

# Argumentos variables para un diccionario


def listarTerminos(**kwargs): #se utiliza ** xq va a recibir un diccionario y kwargs para hacerlo generico para recibir los argumentos
    for llave,valor in kwargs.items(): #kwargs : key word argument
        print(f'{llave} : {valor}')
listarTerminos() #no recibe nada, nada se va a mostrar
listarTerminos(IDE = 'Interface Development Environment', PK = 'Primary Key') #Las llaves no llevan comillas, y el valor puede ser cualquier tipo de dato
listarTerminos(Nombre = 'Leonel Messi') #No acepta un numero como llave

# Distintos tipos de datos como argumentos, definir una funcion q reciba una lista de elementos


def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres2 = ['Tito', 'Pedro', 'Carlos']
desplegarNombres(nombres2)
desplegarNombres('Carla')
# desplegarNombres(10,11) Los numeros no son un objeto iterable xq son int
desplegarNombres((10,11)) #Aca si, xq es una tupla, para poder recorrer estos numeros, pero no puede ser un solo elemento
desplegarNombres([22,55]) # Aca tb se pueden recorrer xq es una lista

# Funciones Recursivas (Caso base y caso Recursivo)


def factorial(numero): # Se envia como argumento y se recibe como parametro
    if numero == 1:
        return 1 # Caso Base
    else:
        return numero * factorial(numero-1) #Caso recursivo

numeroIng = int(input("Por favor ingrese el numero para el cual desea obtener el factorial: "))
resultado = factorial(numeroIng)
#resultado = factorial(5) # Lo hacemos en codigo duro
print(f'El factorial del numero {numeroIng} es : {resultado}')