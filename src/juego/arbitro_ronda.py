class ArbitroRonda:
    def __init__(self):
        pass

    def resultado_duda(self, estado_cachos, pinta, cantidad):
        estado_cachos = estado_cachos
        total_pinta = estado_cachos.get(pinta, 0) + estado_cachos.get(1, 0)
        return total_pinta < cantidad

    def resultado_calzo(self, estado_cachos, pinta, cantidad):
        estado_cachos = estado_cachos
        total_pinta = estado_cachos.get(pinta, 0) + estado_cachos.get(1, 0)
        return total_pinta == cantidad