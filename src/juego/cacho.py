class Cacho:
    __valores = None
    __cantidad = None

    def __init__(self, iniciales=None):
        self.__valores = iniciales
        self.__cantidad = 5
        if iniciales is not None:
            self.__cantidad = len(iniciales)

    def mirar(self):
        return self.__valores