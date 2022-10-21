class Rectangulo:
    '''
    Crear una clase llamada rectangulo, debe tener 2 atributos: altura y base
    el nombre del metodo sera calcular_area utilizando la formula:
    area = base * altura. Pero la base y la altura deben ser ingresadas por el usuario
    y los objetos deben ser tres
    '''

    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    def calcular_area(self):
        area = self.altura * self.base
        return area

altura = int(input("Por favor ingrese la altura del rectangulo: "))
base = int(input("Por favor ingrese la base del rectangulo: "))
rectangulo1 = Rectangulo(altura, base)
print(f'El area del rectangulo es {rectangulo1.calcular_area()}')