class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre # _nombre para encapsular
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalle(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')

    @property  # Decorador
    def nombre(self):  # Método Getter
        print('Estamos usando el metodo get')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):  # Metodo Setter
        print('Estamos usando el metodo set')
        self._nombre = nombre

    @property #Metodo getter
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido): #Metodo setter
        self._apellido = apellido

    @property #Metodo getter
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __del__(self):    #destructor sirve para liberar un espacio después de la creación de un objeto
        print(f'Persona2: {self._nombre} {self._apellido} {self._edad}')

if __name__ == '__main__':
    persona1 = Persona2('Ariel', 'Betancud', 41)
    # persona1._nombre esto no se puede hacer
    print(persona1.nombre)  # LLamamos al metodo getter
    print(persona1.apellido)  # LLamamos al metodo getter
    print(persona1.edad)  # LLamamos al metodo getter

    persona1.nombre = 'Juan Pedro' # LLamamos al método Setter
    print(persona1.nombre)

    print(persona1.mostrar_detalle()) # Llamamos al método mostrar_detalles

    #Atributo read only(solo lectura),sería la edad xq no tiene el
    # método set ya que el método set esta comentado
    # persona1.edad = 40
    print(persona1.edad)
    # Tarea crear tres objetos más utilizando los metodos getter and setter
    # para modificar, y mostrar los cambios
    persona2 = Persona2('Agustin', 'Martinez', 23)
    persona2.nombre = 'Florencia'
    persona2.apellido = 'Romery'
    persona2.edad = 22
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    print(persona2.mostrar_detalle())

    persona3 = Persona2('Caro', 'Felisa', 21)
    persona3.nombre = 'Carolina'
    persona3.apellido = 'Felix'
    persona3.edad = 31
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)
    print(persona3.mostrar_detalle())

    persona4 = Persona2('Naty', 'Lucer', 35)
    persona4.nombre = 'Natalia'
    persona4.apellido = 'Lucero'
    persona4.edad = 33
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4.edad)
    print(persona4.mostrar_detalle())

    print(__name__) #Marcador para decir q hasta aca llega el codigo o sea la clase persona 2
    #Comprobacion del metodo principal para ejecución