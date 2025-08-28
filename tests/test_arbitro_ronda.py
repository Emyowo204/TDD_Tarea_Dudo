import pytest

from src.juego.arbitro_ronda import ArbitroRonda


class TestArbitroRonda:
    @pytest.fixture
    def arbitro(self):
        return ArbitroRonda()
    @pytest.fixture
    def estado_cachos(self):
        return {1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2}  # Simula cantidad de cada dado

    def test_resultado_duda(self, arbitro, estado_cachos):
        pinta = 2
        cantidad = 5
        assert arbitro.resultado_duda(estado_cachos, pinta, cantidad) == True # La duda es correcta

        pinta = 3
        cantidad = 1
        assert arbitro.resultado_duda(estado_cachos, pinta, cantidad) == False # La duda es incorrecta

        pinta = 4
        cantidad = 4
        assert arbitro.resultado_duda(estado_cachos, pinta, cantidad) == False # Cantidad exacta


    def test_resultado_calzo(self, arbitro, estado_cachos):
        pinta = 2
        cantidad = 2
        assert arbitro.resultado_calzo(estado_cachos, pinta, cantidad) == False # El calzo es incorrecto (contando los unos)

        pinta = 3
        cantidad = 4
        assert arbitro.resultado_calzo(estado_cachos, pinta, cantidad) == True # El calzo es correcto (contando los unos)


    def test_validador_calzo(self, arbitro, estado_cachos):
        cantidad_cachos = 6
        assert arbitro.validar_calzo(estado_cachos, cantidad_cachos) == False # Hay menos de la mitad de dados

        assert arbitro.validar_calzo(estado_cachos, cantidad_cachos, True) == True # Existe un jugador con 1 dado

        cantidad_cachos = 3
        assert arbitro.validar_calzo(estado_cachos, cantidad_cachos) == True # Hay más de la mitad de dados

        assert arbitro.validar_calzo(estado_cachos, cantidad_cachos, True) == True # Existe un jugador con 1 dado y hay más de la mitad de dados