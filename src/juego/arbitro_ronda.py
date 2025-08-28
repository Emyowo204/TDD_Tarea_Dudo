class ArbitroRonda:
    def __init__(self):
        pass

    @staticmethod
    def _total_pinta(estado_cachos, pinta):
        """
        Retorna la cantidad total de cachos que hay de una pinta determinada,
        incluyendo los cachos comodín (pinta 1).
        :param estado_cachos: Diccionario con la cantidad de dados con cierta pinta.
        :param pinta: La pinta a verificar.
        :return: Cantidad total de cachos de la pinta especificada.
        """
        return estado_cachos.get(pinta, 0) + estado_cachos.get(1, 0)

    def resultado_duda(self, estado_cachos, pinta, cantidad):
        """
        Retorna si la duda fue correcta (si la cantidad de dados de la pinta
        especificada es menor a la cantidad apostada).
        :param estado_cachos: Diccionario con la cantidad de dados con cierta pinta.
        :param pinta: La pinta a verificar.
        :param cantidad: La cantidad apostada.
        :return: True si la duda fue correcta, False en caso contrario.
        """
        return self._total_pinta(estado_cachos, pinta) < cantidad

    def resultado_calzo(self, estado_cachos, pinta, cantidad):
        """
        Retorna si el calzo fue correcto (si la cantidad de dados de la pinta
        especificada es igual a la cantidad apostada).
        :param estado_cachos: Diccionario con la cantidad de dados con cierta pinta.
        :param pinta: La pinta a verificar.
        :param cantidad: La cantidad apostada.
        :return: True si el calzo fue correcto, False en caso contrario.
        """
        return self._total_pinta(estado_cachos, pinta) == cantidad

    def validar_calzo(self, estado_cachos, cantidad_cachos, existe_jugador_con_un_dado=False):
        if existe_jugador_con_un_dado:
            return True
        total_dados = sum(estado_cachos.values())
        if total_dados >= (cantidad_cachos * 5) / 2:
            return True
        return False