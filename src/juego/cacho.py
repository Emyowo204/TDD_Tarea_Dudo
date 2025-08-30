from src.juego.dado import Dado

class Cacho:
    __valores = None
    __cantidad = None
    __dado = None

    def __init__(self, iniciales=None):
        self.__valores = iniciales
        self.__cantidad = 5
        self.__dado = Dado()
        if iniciales is not None:
            self.__cantidad = len(iniciales)

    def mirar(self):
        return self.__valores

    def agitar(self):
        self.__valores = []
        for i in range(self.__cantidad):
            self.__valores.append(self.__dado.lanzar())

    def quitar_dado(self):
        if self.__cantidad > 0:
            self.__cantidad -= 1
            self.agitar()

    def agregar_dado(self):
        self.__cantidad += 1
        self.agitar()
