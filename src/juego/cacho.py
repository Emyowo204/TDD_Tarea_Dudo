class Cacho:
    __valores = None

    def __init__(self, iniciales=None):
        self.__valores = iniciales

    def mirar(self):
        return self.__valores