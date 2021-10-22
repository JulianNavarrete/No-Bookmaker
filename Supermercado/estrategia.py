from producto import Producto
from carrito import Carrito


if __name__ == '__main__':
    coca = Producto(50, '1234', 'bebida')
    pan = Producto(100, '321', 'lactal')
    carne = Producto(700, '456', 'molida')
    carrito = Carrito()
    carrito.agregar(coca, 2)
    carrito.agregar(pan, 1)
    carrito.agregar(carne, 10)
    print(carrito.esta_vacio())
    for p in carrito.obtener_todos():
        print(f'{p.codigo}\t{p.descripcion}\t{carrito.obtener_todos().get(p)}')

    carrito.vaciar()
    print(carrito.esta_vacio())
