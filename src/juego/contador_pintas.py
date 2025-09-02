from src.juego.cacho import Cacho

""" Contador de apariciones de una pinta específica en uno o más cachos. """
class Contador_Pintas:

    def contar_pintas(self, cacho, pinta):
        """
        Contar las apariciones de una pinta específica dentro de un (1) cacho,
        contando los Ases como comodines.
        :param cacho: Cacho el cual contiene los dados a contar.
        :param pinta: La pinta específica a contar (Contando los Ases).
        :return: Cantidad total de la pinta especificada, contando Ases.
        """
        cantidad = 0
        for valor in cacho.mirar():
            if valor == pinta or valor == 'As':
                cantidad += 1
        return cantidad

    def contar_pintas_sinAs(self, cacho, pinta):
        """
        Contar las apariciones de una pinta específica dentro de un (1) cacho,
        SIN contar a los Ases como comodines.
        :param cacho: Cacho el cual contiene los dados a contar.
        :param pinta: La pinta específica a contar.
        :return: Cantidad total de la pinta especificada.
        """
        cantidad = 0
        for valor in cacho.mirar():
            if valor == pinta:
                cantidad += 1
        return cantidad

    def contar_pintas_totales(self, lista_cachos, pinta):
        """
        Contar las apariciones de una pinta específica dentro de un grupo de cachos,
        contando los Ases como comodines.
        :param lista_cachos: Lista de los cachos los cuales contiene los dados a contar.
        :param pinta: La pinta específica a contar (Contando los Ases).
        :return: Cantidad total de la pinta especificada, contando Ases.
        """
        cantidad = 0
        for cacho in lista_cachos:
            cantidad += self.contar_pintas(cacho, pinta)
        return cantidad

    def contar_pintas_totales_sinAs(self, lista_cachos, pinta):
        """
        Contar las apariciones de una pinta específica dentro de un grupo de cachos,
        SIN contar a los Ases como comodines.
        :param lista_cachos: Lista de los cachos los cuales contiene los dados a contar.
        :param pinta: La pinta específica a contar.
        :return: Cantidad total de la pinta especificada.
        """
        cantidad = 0
        for cacho in lista_cachos:
            cantidad += self.contar_pintas_sinAs(cacho, pinta)
        return cantidad