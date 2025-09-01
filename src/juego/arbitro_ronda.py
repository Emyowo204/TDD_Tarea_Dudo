class ArbitroRonda:
    def __init__(self):
        pass

    @staticmethod
    def _total_pinta(estado_cachos, pinta, obligar = False):
        """
        Retorna la cantidad total de cachos que hay de una pinta determinada,
        incluyendo los cachos comodín (pinta 1).
        :param estado_cachos: Diccionario con la cantidad de dados con cierta pinta.
        :param pinta: La pinta a verificar.
        :param obligar: Indica si existe un jugador con un solo dado.
        :return: Cantidad total de cachos de la pinta especificada.
        """
        if not obligar:
            if pinta != 1:
                return estado_cachos.get(pinta, 0) + estado_cachos.get(1, 0)
            return estado_cachos.get(1, 0)
        return estado_cachos.get(pinta, 0)


    def resultado_duda(self, estado_cachos, pinta, cantidad, obligar = False):
        """
        Retorna si la duda fue correcta (si la cantidad de dados de la pinta
        especificada es menor a la cantidad apostada).
        :param estado_cachos: Diccionario con la cantidad de dados con cierta pinta.
        :param pinta: La pinta a verificar.
        :param cantidad: La cantidad apostada.
        :param obligar: Indica si existe un jugador con un solo dado.
        :return: True si la duda fue correcta, False en caso contrario.
        """
        return self._total_pinta(estado_cachos, pinta, obligar) < cantidad

    def resultado_calzo(self, estado_cachos, pinta, cantidad, obligar = False):
        """
        Retorna si el calzo fue correcto (si la cantidad de dados de la pinta
        especificada es igual a la cantidad apostada).
        :param estado_cachos: Diccionario con la cantidad de dados con cierta pinta.
        :param pinta: La pinta a verificar.
        :param cantidad: La cantidad apostada.
        :param obligar: Indica si existe un jugador con un solo dado.
        :return: True si el calzo fue correcto, False en caso contrario.
        """
        return self._total_pinta(estado_cachos, pinta, obligar) == cantidad

    @staticmethod
    def validar_calzo(estado_cachos, cantidad_cachos, existe_jugador_con_un_dado=False):
        """
        Valida si el calzo se puede hacer (hay más de la mitad de los dados en juego o
        hay un jugador con un solo dado)
        :param estado_cachos: Diccionario con la cantidad de dados con cierta pinta.
        :param cantidad_cachos: Cantidad total de cachos en juego.
        :param existe_jugador_con_un_dado: Booleano que indica si hay un jugador con un solo dado.
        :return: True si el calzo es válido, False en caso contrario.
        """
        if existe_jugador_con_un_dado:
            return True

        return sum(estado_cachos.values()) >= (cantidad_cachos * 5) / 2
