from pytest_mock import mocker

from src.ArbitroRonda import ArbitroRonda


class TestArbitroRonda:
    def test_resultado_duda(self):
        arbitro = ArbitroRonda()
        mock_get_estado_cachos = mocker.patch('src.GestorPartida.get_estado_cachos')
        mock_get_estado_cachos.return_value = {1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2}  # Simula cantidad de cada dado

        pinta = 2
        cantidad = 5
        assert arbitro.resultado_duda(mock_get_estado_cachos, pinta, cantidad) == True # La duda es correcta

        pinta = 3
        cantidad = 1
        assert arbitro.resultado_duda(mock_get_estado_cachos, pinta, cantidad) == False # La duda es incorrecta

        pinta = 4
        cantidad = 4
        assert arbitro.resultado_duda(mock_get_estado_cachos, pinta, cantidad) == True # La duda es correcta (contando los unos)


    def test_resultado_calzo(self):
        arbitro = ArbitroRonda()
        mock_get_estado_cachos = mocker.patch('src.GestorPartida.get_estado_cachos')
        mock_get_estado_cachos.return_value = {1: 1, 2: 3, 3: 2, 4: 0, 5: 0, 6: 0} # Simula cantidad de cada dado

        pinta = 2
        cantidad = 3
        assert arbitro.resultado_calzo(mock_get_estado_cachos, pinta, cantidad) == False # El calzo es incorrecto (contando los unos)

        pinta = 3
        cantidad = 3
        assert arbitro.resultado_calzo(mock_get_estado_cachos, pinta, cantidad) == True # El calzo es correcto (contando los unos)