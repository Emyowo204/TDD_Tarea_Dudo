import math

class Validador_Apuesta:

    __pintas = ['As', 'Tonto', 'Tren', 'Cuadra', 'Quina', 'Sexto']

    def __convertir(self, pinta):
        for i in range(len(self.__pintas)):
            if self.__pintas[i] == pinta:
                return i+1
        return 0

    def __esPar(self, numero):
        return numero % 2 == 0

    def validar(self, numIni, pintaIni, numNuevo, pintaNueva):
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
            if self.__esPar(numIni) and numNuevo >= (numIni / 2) + 1:
                return True
            if not self.__esPar(numIni) and numNuevo >= math.ceil(numIni / 2):
                return True

        else:
            if numNuevo > numIni:
                return True
            if numNuevo == numIni and self.__convertir(pintaNueva) > self.__convertir(pintaIni):
                return True
        return False

