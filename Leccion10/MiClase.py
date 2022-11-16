class MiClase:
    # Variable de clase, este atributo dara a cada objeto el mismo valor
    variable_clase = 'Esta es una variable de clase'

    def __init__(self, variable_instancia):  # La variable de instancia, da diferentes valores
        self.variable_instancia = variable_instancia

    @staticmethod
    def metodo_estatico(): #El metodo estatico se asocia a la clase, no recibe informacion relacionada con la clase
        print(MiClase.variable_clase)

    @classmethod
    def metodo_clase(cls): #un metodo de clase si recibe un contexto de clase, cls es una referencia a la clase, se puede
        print(cls.variable_clase) #utilizar otra palabra

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_clase)
        print(self.variable_instancia)


print(MiClase.variable_clase)

miClase1 = MiClase('Esta es una variable de instancia')
print(miClase1.variable_instancia)
print(miClase1.variable_clase)

miClase2 = MiClase('Esta es otra prueba de variable de instancia')
print(miClase2.variable_instancia)
print(miClase2.variable_clase)

MiClase.variable_clase2 = 'Valor de variable de clase 2'
print(MiClase.variable_clase2)
print(miClase1.variable_clase2)
print(miClase2.variable_clase2)

MiClase.metodo_estatico()

MiClase.metodo_clase()
miObjeto1 = MiClase('variable de instancia')
miObjeto1.metodo_clase() # Las clases es el contexto estatico y no pueden acceder al dinamico
miObjeto1.metodo_instancia()