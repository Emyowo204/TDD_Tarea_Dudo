from src.juego.dado import Dado

""" Cacho que puede contener dados, utilizado en el juego Dudo. """
class Cacho:

    """ Nombre de las pintas de cada dado dentro del cacho. """
    __valores = None
    """ Cantidad de dados dentro del cacho. """
    __cantidad = None
    """ Intancia del dado utilizada para los dados dentro del cacho. """
    __dado = None

    def __init__(self, iniciales=None):
        """
        Constructor de un cacho con 5 dados, a excepción que se inicialicen los mismos.
        :param iniciales: Lista de pintas de los dados con los que se quiere iniciar el cacho, no es obligatoria.
        """
        self.__valores = iniciales
        self.__cantidad = 5
        self.__dado = Dado()
        if iniciales is not None:
            self.__cantidad = len(iniciales)

    def mirar(self):
        """
        Se utiliza para poder ver los dados dentro del cacho.
        :return: Una lista con las pintas de los dados en el cacho.
        """
        return self.__valores

    def agitar(self):
        """
        Se utiliza para poder agitar los dados y generar nuevos valores de los mismos.
        """
        self.__valores = []
        for i in range(self.__cantidad):
            self.__valores.append(self.__dado.lanzar())

    def quitar_dado(self):
        """
        Quita uno de los dados dentro del cacho, no puede ser menor a 0.
        """
        if self.__cantidad > 0:
            self.__cantidad -= 1
            self.agitar()

    def agregar_dado(self):
        """
        Agrega un nuevo dado al cacho, no tiene limite predeterminado.
        """
        self.__cantidad += 1
        self.agitar()
