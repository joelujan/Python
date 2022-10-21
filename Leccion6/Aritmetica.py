class Aritmetica:
    """
     El nombre de este tipo de comentario es : DocString
     esto es documentación de la clase en Python
     Vamos a hacer en esta clase algunas operaciones de: suma, resta, multiplicación y más
    """

    def __init__(self, operandoA, operandoB):  # Init Dunder
        self.operandoA = operandoA
        self.operandoB = operandoB

    # Metodo para sumar
    def sumar(self):
        return self.operandoA + self.operandoB

    def resta(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB

    def dividir(self):
        return self.operandoA / self.operandoB

aritmetica1 = Aritmetica(7, 9)  # Le pasamos los argumentos para los operandos
print(f'La suma de los numeros es: {aritmetica1.sumar()}')
print(f'La resta de los numeros es: {aritmetica1.resta()}')
print(f'La multiplicacion de los numeros es: {aritmetica1.multiplicar()}')
print(f'La division de los numeros es: {aritmetica1.dividir():}.2f') #.2f para que muestre solo 2 numeros flotantes
