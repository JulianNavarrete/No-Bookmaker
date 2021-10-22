from producto import Producto


class Carrito():
    __productos = {}

    def agregar(self, producto: Producto, cantidad: int):
        self.__productos[producto] = cantidad + self.__productos.get(producto, 0)

    def borrar(self, clave: str):
        self.__productos.pop(clave)

    def modificar(self, clave: str, producto):
        self.borrar(clave)
        self.agregar(producto)

    def obtener_producto(self, clave: str):
        return self.__productos[clave]

    def obtener_todos(self, ):
        return self.__productos

    def total_precio(self):
        suma = 0
        for p in self.__productos:
            suma += p.precio
        return suma

    def esta_vacio(self):
        if len(self.__productos) == 0:
            return True
        return False

