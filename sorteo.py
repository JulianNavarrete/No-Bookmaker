from selector_logica import Alumno
import random
import time

class SorteoLista():

    __lista = []
    __seleccion = []
    def agregar(self, alumno:Alumno):
        self.__lista.append(alumno)

    def seleccionar(self):
        self.__lista.sort(key=lambda x: x.puntaje)
        mitad = int(len(self.__lista) / 2)
        for i in range(mitad):
               self.__seleccion.append(self.__lista[i])
               print("Seleccionados: ", self.__lista[i])

    def elegir(self):
        random.seed(time.time())
        print(random.choice(self.__seleccion))


