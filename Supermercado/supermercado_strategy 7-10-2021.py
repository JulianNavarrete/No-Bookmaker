from abc import ABC, abstractmethod


class EstrategiaDescuento(ABC):
    @abstractmethod
    def calcular_precio_con_descuento(self):
        pass


class Estrategia_Descuento_Cantidad(EstrategiaDescuento):

    def calcular_precio_con_descuento(self, cantidad):
        descuento = 0
        if cantidad > 0:
            descuento = 0
            if cantidad == 1:
                descuento = 0
            if 5 <= cantidad <= 20:
                descuento = self.__precio * 0.15
            if 20 <= cantidad <= 50:
                descuento = self.__precio * 0.21
            if cantidad > 50:
                descuento = self.__precio * 0.30
        return descuento


class Estrategia_Descuento_Dias(EstrategiaDescuento):

    def calcular_precio_con_descuento(self, cantidad, dia):
        if dia == 3:
            descuento = self.precio * 0.20
        if dia == 5:
            descuento = self.precio * 0.35
        return descuento


class Estrategia_Descuento_Mayorista(EstrategiaDescuento):

    def calcular_precio_con_descuento(self, cantidad):
        pass


class ProductoContext:

    def __init__(self, precio, estrategia:EstrategiaDescuento):
        self.__precio = precio
        self.__estrategia = estrategia

    def calcular_precio(self):
        self.__estrategia.calcular_precio_con_descuento(self.__precio)

