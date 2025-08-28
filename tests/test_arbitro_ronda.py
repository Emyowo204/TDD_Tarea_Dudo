from src.juego.arbitro_ronda import ArbitroRonda


class TestArbitroRonda:
    def test_resultado_duda(self):
        arbitro = ArbitroRonda()
        estado_cachos = {1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2}  # Simula cantidad de cada dado

        pinta = 2
        cantidad = 5
        assert arbitro.resultado_duda(estado_cachos, pinta, cantidad) == True # La duda es correcta

        pinta = 3
        cantidad = 1
        assert arbitro.resultado_duda(estado_cachos, pinta, cantidad) == False # La duda es incorrecta

        pinta = 4
        cantidad = 4
        assert arbitro.resultado_duda(estado_cachos, pinta, cantidad) == False # Cantidad exacta


    def test_resultado_calzo(self):
        arbitro = ArbitroRonda()
        estado_cachos = {1: 1, 2: 3, 3: 2, 4: 0, 5: 0, 6: 0} # Simula cantidad de cada dado

        pinta = 2
        cantidad = 3
        assert arbitro.resultado_calzo(estado_cachos, pinta, cantidad) == False # El calzo es incorrecto (contando los unos)

        pinta = 3
        cantidad = 3
        assert arbitro.resultado_calzo(estado_cachos, pinta, cantidad) == True # El calzo es correcto (contando los unos)