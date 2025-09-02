from src.servicios.generador_aleatorio import generar_numero_aleatorio

""" Dado de 6 caras utilizando nombres del juego Dudo. """
class Dado:

    """ Lista con los nombres de las pintas del dado, de 1 a 6. """
    __pintas = ['As', 'Tonto', 'Tren', 'Cuadra', 'Quina', 'Sexto']

    def lanzar(self):
        """
        Lanza un dado de 6 caras con el nombre de las pintas del juego Dudo.
        :return: Nombre de 1 de las 6 pintas, generada semi-aleatoriamente.
        """
        return self.__pintas[generar_numero_aleatorio(0,5)]
