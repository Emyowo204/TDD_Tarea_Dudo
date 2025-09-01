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

    def test_num_jugadores_invalido(self):

        # Probar con un número de jugadores inválido (menos de 2)
        with pytest.raises(ValueError):
            GestorPartida(0)
        with pytest.raises(ValueError):
            GestorPartida(1)

        # Probar con otro tipo de dato
        with pytest.raises(TypeError):
            GestorPartida("tres")

    def test_empate_iniciar_partida(self, gestor):

        # Primera ronda: empate entre jugadores 1 y 4
        with patch('src.juego.gestor_partida.generar_lista_aleatoria', side_effect=[
            [3, 2, 1, 3, 2, 1],     # Empatan jugador 1 y 4
            [2, 5]                  # Relanzan solo los empatados
        ]):
            gestor.iniciar_partida()
            # El turno debe ser del jugador 4 (5 es el mayor en el relanzamiento)
            assert gestor.turno_actual == 3

    def test_determinar_siguiente_jugador(self, gestor):
        gestor.turno_actual = 2
        gestor.avanzar_turno()
        # El siguiente jugador debe ser el 3
        assert gestor.turno_actual == 3

        gestor.turno_actual = 5
        gestor.avanzar_turno()
        # El siguiente jugador debe ser el 0 (ciclo)
        assert gestor.turno_actual == 0

    def test_convertir_diccionario(self, gestor):
        gestor.jugadores = [
            [1, 2, 3, 4, 5],
            [2, 3, 4, 5, 6],
            [3, 4, 5, 6, 6],
            [4, 5, 6, 6, 6]
        ]
        diccionario = gestor._convertir_a_diccionario()
        # Verificar que se ha creado un diccionario
        assert isinstance(diccionario, dict)

        esperado = {1:1, 2:2, 3:3, 4:4, 5:4, 6:6}
        # Verificar que el diccionario generado es correcto
        assert diccionario == esperado