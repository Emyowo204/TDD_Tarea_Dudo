from src.servicios.generador_aleatorio import generar_numero_aleatorio

class Dado:
    __pintas = ['As', 'Tonto', 'Tren', 'Cuadra', 'Quina', 'Sexto']

    def lanzar(self):
        return self.__pintas[generar_numero_aleatorio(0,5)]
