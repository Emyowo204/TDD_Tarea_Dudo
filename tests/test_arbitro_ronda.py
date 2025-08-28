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
        # La duda es correcta
        assert arbitro.resultado_duda(estado_cachos, pinta, cantidad) == True

        pinta = 3
        cantidad = 1
        # La duda es incorrecta
        assert arbitro.resultado_duda(estado_cachos, pinta, cantidad) == False

        pinta = 4
        cantidad = 4
        # Cantidad exacta
        assert arbitro.resultado_duda(estado_cachos, pinta, cantidad) == False

    def test_resultado_calzo(self, arbitro, estado_cachos):
        pinta = 2
        cantidad = 2
        # El calzo es incorrecto (contando los unos)
        assert arbitro.resultado_calzo(estado_cachos, pinta, cantidad) == False

        pinta = 3
        cantidad = 4
        # El calzo es correcto (contando los unos)
        assert arbitro.resultado_calzo(estado_cachos, pinta, cantidad) == True

    def test_validador_calzo(self, arbitro, estado_cachos):
        cantidad_cachos = 6
        # Hay menos de la mitad de dados
        assert arbitro.validar_calzo(estado_cachos, cantidad_cachos) == False
        # Existe un jugador con 1 dado
        assert arbitro.validar_calzo(estado_cachos, cantidad_cachos, True) == True

        cantidad_cachos = 3
        # Hay más de la mitad de dados
        assert arbitro.validar_calzo(estado_cachos, cantidad_cachos) == True
        # Existe un jugador con 1 dado y hay más de la mitad de dados
        assert arbitro.validar_calzo(estado_cachos, cantidad_cachos, True) == True

    def test_casos_especiales(self, arbitro, estado_cachos):
        # Caso especial: La apuesta es de ases
        pinta = 1
        cantidad = 4  # Más que la cantidad de ases
        assert arbitro.resultado_duda(estado_cachos, pinta, cantidad) == True

        assert arbitro.resultado_calzo(estado_cachos, pinta, cantidad) == False

        cantidad = 2  # Exactamente la cantidad de ases
        assert arbitro.resultado_duda(estado_cachos, pinta, cantidad) == False

        assert arbitro.resultado_calzo(estado_cachos, pinta, cantidad) == True

        # Caso especial: Jugador con un dado (Obligar)
        pinta = 3
        cantidad = 4  # Más que la cantidad de trenes sin contar comodínes
        assert arbitro.resultado_duda(estado_cachos, pinta, cantidad, True) == True

        assert arbitro.resultado_calzo(estado_cachos, pinta, cantidad, True) == False

        cantidad = 2  # La cantidad justa de trenes sin contar comodínes
        assert arbitro.resultado_duda(estado_cachos, pinta, cantidad, True) == False

        assert arbitro.resultado_calzo(estado_cachos, pinta, cantidad, True) == True
