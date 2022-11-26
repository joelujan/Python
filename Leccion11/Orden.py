from Producto import Producto


class Orden:
    contador_ordenes = 0

    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self.id_orden = Orden.contador_ordenes
        self._productos = list(productos)  # convertimos los productos a una lista.

    def agregar_producto(self, producto):
        self._productos.append(producto)  # para agregar un nuevo producto con la funcion append

    def calcular_total(self):
        total = 0  # Variable temporal para almacenar el total temporal
        for producto in self._productos:
            total += producto.precio  # aca estamos usando el del get precio
        return total

    def __str__(self):
        productos_str = ''
        for producto in self._productos:
            productos_str += producto.__str__() + '|'  # Concatenamos todos los productos
        return f'Orden: {self.id_orden}, \nProducto: {productos_str}'


if __name__ == '__main__':
    producto1 = Producto('Camiseta', 100.00)
    producto2 = Producto('Pantalon', 150.00)
    productos1 = [producto1, producto2]  # Lista de productos

    producto3 = Producto('Medias', 50.00)
    producto4 = Producto('Calzoncillos', 70.00)
    producto5 = Producto('Remera', 90.00)
    productos2 = [producto3, producto4, producto5]
    orden1 = Orden(productos1)  # Primer Objeto Orden pasando la lista de productos
    print(orden1)
    orden2 = Orden(productos2)
    print(orden2)

# Tarea: Modificar la orden2 ingresando nuevos productos con sus nombres y precios
# crear una nueva lista de productos y agregarla a la orden2
