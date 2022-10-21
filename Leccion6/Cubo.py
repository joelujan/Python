class Cubo:
    '''
    Crear la clase Cubo con los atributos, ancho, alto y profundidad, con un
    método calcular_volumen que tendrá la fórmula: volumen = ancho * altura * profundidad
    que el usuario ingrese los valores
    '''

    def __init__(self, ancho, altura, profundidad):
        self.ancho = ancho
        self.altura = altura
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.altura * self.profundidad * self.ancho

ancho = int(input("Por favor ingrese el ancho del cuerpo que desea, para calcular el volumen:"))
altura = int(input("Por favor ingrese la altura del cuerpo que desea, para calcular el volumen:"))
profundidad = int(input("Por favor ingrese la profundidad del cuerpo que desea, para calcular el volumen:"))

cubo1 = Cubo(ancho, altura, profundidad)
print(f'El volumen del cubo es: {cubo1.calcular_volumen()}')

