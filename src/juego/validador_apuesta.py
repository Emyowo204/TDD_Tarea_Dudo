import math

""" Valida si una nueva apuesta con respecto a las condiciones de la apuesta anterior. """
class Validador_Apuesta:

    """ Lista con los nombres de las pintas del dado, de 1 a 6. """
    __pintas = ['As', 'Tonto', 'Tren', 'Cuadra', 'Quina', 'Sexto']

    def __convertir(self, pinta):
        """
        Convierte una pinta del juego Dudo en su valor numérico.
        :param pinta: La pinta a convertir.
        :return: El valor numérico de la pinta convertida (Del 1 al 6).
        """
        numero = 0
        for i in range(len(self.__pintas)):
            if self.__pintas[i] == pinta:
                numero = i+1
        return numero

    def validar(self, numIni, pintaIni, numNuevo, pintaNueva):
        """
        Validación de la apuesta realizada, según la apuesta anterior.
        :param numIni: La cantidad de la apuesta anterior.
        :param pintaIni: La pinta de la apuesta anterior.
        :param numNuevo: La cantidad de la apuesta realizada actualmente.
        :param pintaNueva: La pinta de la apuesta realizada actualmente.
        :return: Booleano con la validación de la apuesta (Valida / No valida).
        """
        if pintaIni == None and (pintaNueva == 'As' or numNuevo <=0):
            return False

        if pintaIni == pintaNueva == 'As':
            if numNuevo > numIni:
                return True
            return False

        elif pintaIni == 'As':
            if numNuevo >= (numIni*2)+1:
                return True
            return False

        elif pintaNueva == 'As':
            if numIni % 2 == 0 and numNuevo >= (numIni / 2) + 1:
                return True
            if numIni % 2 != 0 and numNuevo >= math.ceil(numIni / 2):
                return True

        else:
            if numNuevo > numIni:
                return True
            if numNuevo == numIni and self.__convertir(pintaNueva) > self.__convertir(pintaIni):
                return True
        return False

