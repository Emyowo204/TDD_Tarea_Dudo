from unittest.mock import patch
import pytest
from src.juego.gestor_partida import GestorPartida

class TestGestorPartida:
    @pytest.fixture
    def gestor(self):
        return GestorPartida(6)

    def test_inicializar_jugadores(self, gestor):

        # Verificar que se han creado 6 jugadores
        assert len(gestor.jugadores) == 6

    def test_iniciar_partida(self, gestor):
        with patch('src.juego.gestor_partida.generar_lista_aleatoria', return_value=[1, 2, 3, 4, 5, 6]):
            gestor.iniciar_partida()

            # El turno inicial debe ser del jugador 6 (obtuvo el número más alto)
            assert gestor.turno_actual == 5