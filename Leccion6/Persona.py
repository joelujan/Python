class Persona:  # Creamos una clase
    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs):  # método para inicializar un objeto. Self es el parametro por default
        # Init Dunder asi se le llama al metodo
        self.nombre = nombre
        #self.__saraza = saraza #Doble guion bajo ESTE TIPO DE DATO NO SE MUESTRA DIRECTAMENTE
        self.apellido = apellido
        self._dni = dni #ENCAPSULAMIENTO, este atributo esta encapsulado de una manera sugerida
        self.edad = edad
        self.args = args #*argumento variable tupla
        self.kwargs = kwargs #**Diccionario con argumentos variables Valor del diccionario

    def mostrar_detalle(self):  # self es un metodo de instancia, self es igual a this
        print(f'La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self._dni} {self.edad}, la '
              f'dirección es: {self.args}, los datos importantes son {self.kwargs}')
    # la variable self solo se encuentra dentro de los métodos.


persona1 = Persona('Ariel', 'Betancud',3456456564, 40)  # Necesitamos enviar argumentos
# print(persona1.nombre)
# print(persona1.apellido)
# print(persona1.edad)
print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido}. Su edad es: {persona1.edad}')

persona2 = Persona('Osvaldo', 'Giordanini', 30111586, 45)
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido}. Su edad es: {persona2.edad}')

persona1.nombre = 'Liliana'
persona1.apellido = 'Bucella'
persona1.edad = 40
print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido}. Su edad es: {persona1.edad}')

# Los atributos son caracteristicas
# Los métodos son el comportamiento que van a tener los objetos (acciones)
persona1.mostrar_detalle()# La referencia se pasa de manera automatica
persona2.mostrar_detalle()
# Persona.mostrar_detalle(persona1) #Debemos pasarle una referencia para el self o dará error

persona1.telefono = '44445555289' #Hemos creado un atributo desde un objeto, superficialmente
print(f'Este es el telefono: {persona1.nombre}, {persona1.telefono}')

# print(persona2.telefono) el objeto persona2 no tiene este atributo, da error.
persona3 = Persona('Rogelio', 'Romero', 39888756, 22, 'Teléfono', '2614445557', "Calle Lopez", 823, 'Manzana', 77, 'Casa', 18,
                   Altura=1.83, Peso=105, CFavorito = 'Azul', Auto='Citroen', Modelo=2021)
#Tupla desde Telefono
#Diccionario desde Altura
persona3.mostrar_detalle()

#print(persona3.dni)# no lo encuentra porque esta "Como encapsulado",
#print(persona3._dni)# Y de esta manera lo encuentra, pero no debe utilizarse en python,(esta encapsulado) esto dice q desconocemos python

#persona3.__zaraza #esta totalmente encapsulado, no se puede mostrar, no va a aceptar ningun cambio