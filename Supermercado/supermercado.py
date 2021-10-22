from datetime import datetime

class Producto:

    def _init__(self, precio):
        #self.__codigo = codigo
        self.__precio = precio
        #self.__descripcion = descripcion
       
        

    def precio(self, precio, cantidad):
        if cantidad > 0:
            
            if cantidad == 1:
                descuento = 0
            if 5 <= cantidad <= 20:
                descuento = precio * 0.15
            if 20 > cantidad <= 50:
                descuento = precio * 0.21
            if cantidad > 50:
                descuento = precio * 0.30

        precio_final = (precio - descuento) * cantidad
        return print(precio_final)


    def precio(self, precio):
        if dias_semana == 3:
            descuento = precio * 0.20
        elif dias_semana == 5:
            descuento = precio * 0.35
        
        precio_final2 = (precio - descuento)
        return print(precio_final2)


producto = Producto()
precio = float(input("Digite el precio:"))
cantidad = int(input("Cantidad:"))
dias_semana = input("Ingregar dia por numero:") #ej : domingo n° 0
producto.precio(precio)
