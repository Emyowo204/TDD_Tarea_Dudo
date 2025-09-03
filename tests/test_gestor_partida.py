from unittest.mock import patch
import pytest
from src.juego.gestor_partida import GestorPartida
from src.juego.cacho import Cacho

class TestGestorPartida:
    @pytest.fixture
    # Proveer un gestor de partida con 6 jugadores para las pruebas
    def gestor(self):
        return GestorPartida(6)

    @staticmethod
    # Crear cachos con valores específicos para pruebas
    def crear_cachos():
        return [Cacho([1, 2, 3, 4, 5]),
                Cacho([2, 3, 4, 5, 6]),
                Cacho([3, 4, 5, 6, 6]),
                Cacho([4, 5, 6, 6, 6])]

    def test_inicializar_jugadores(self, gestor):

        # Verificar que se han creado 6 jugadores
        assert len(gestor.jugadores) == 6

    def test_iniciar_partida(self, gestor):
        with patch('src.juego.gestor_partida.generar_lista_aleatoria', return_value=[1, 2, 3, 4, 5, 6]):
            gestor.iniciar_partida()

            # El turno inicial debe ser del jugador 6 (obtuvo el número más alto)
            assert gestor.turno[0] == 5

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
            assert gestor.turno[0] == 3

    def test_determinar_siguiente_jugador(self, gestor):
        gestor.turno.rotate(-2)
        gestor.avanzar_turno()
        # El siguiente jugador debe ser el 3
        assert gestor.turno[0] == 3

        gestor.turno.rotate(-2)
        gestor.avanzar_turno()
        # El siguiente jugador debe ser el 0 (ciclo)
        assert gestor.turno[0] == 0

    def test_convertir_diccionario(self, gestor):
        # Asignar dados específicos a los jugadores para la prueba
        gestor.jugadores = self.crear_cachos()
        diccionario = gestor._convertir_a_diccionario()
        # Verificar que se ha creado un diccionario
        assert isinstance(diccionario, dict)

        esperado = {1:1, 2:2, 3:3, 4:4, 5:4, 6:6}
        # Verificar que el diccionario generado es correcto
        assert diccionario == esperado

    def test_procesar_apuestas(self, gestor):
        gestor.jugadores = self.crear_cachos()
        apuestas = [
            (2, 'Tonto'),   # válida
            (0, 'Tonto'),   # inválida
            (3, 'Tonto')    # válida
        ]
        turnos = [1, 1, 2]  # El turno no avanza tras la apuesta inválida

        for apuesta, esperado_turno in zip(apuestas, turnos):
            if apuesta[0] == 0:
                with pytest.raises(ValueError):
                    gestor.procesar_apuesta(apuesta)
            else:
                gestor.procesar_apuesta(apuesta)
            assert gestor.turno[0] == esperado_turno

    def test_llamar_arbitro_calzo_correcto(self, gestor):
        gestor.jugadores = self.crear_cachos()
        gestor.turno[0] = 0
        gestor.procesar_apuesta((3, 'Tonto'))
        gestor.llamar_arbitro("calzo")
        # El calzo es correcto, jugador 2 debe ganar un dado
        assert len(gestor.jugadores[1].mirar()) == 6
        assert gestor.apuesta_actual == (0, None)

    def test_llamar_arbitro_calzo_incorrecto(self, gestor):
        gestor.jugadores = self.crear_cachos()
        gestor.procesar_apuesta((4, 'Tonto'))
        gestor.llamar_arbitro("calzo")
        # El calzo es incorrecto, jugador 2 pierde un dado
        assert len(gestor.jugadores[1].mirar()) == 4
        assert gestor.apuesta_actual == (0, None)

    def test_llamar_arbitro_duda_incorrecta(self, gestor):
        gestor.jugadores = self.crear_cachos()
        gestor.turno.rotate(-1)
        gestor.procesar_apuesta((3, 'Tonto'))
        gestor.llamar_arbitro("duda")
        # La duda es incorrecta, jugador 3 pierde un dado
        assert len(gestor.jugadores[2].mirar()) == 4
        assert gestor.apuesta_actual == (0, None)

    def test_llamar_arbitro_duda_correcta(self, gestor):
        gestor.jugadores = self.crear_cachos()
        gestor.turno.rotate(-3)
        gestor.procesar_apuesta((4, 'Tonto'))
        gestor.llamar_arbitro("duda")
        # La duda es correcta, jugador 4 pierde un dado
        assert len(gestor.jugadores[3].mirar()) == 4
        assert gestor.apuesta_actual == (0, None)

    def test_jugador_eliminado(self, gestor):
        gestor.jugadores = self.crear_cachos()
        gestor.jugadores.append(Cacho([]))
        gestor.turno.pop()
        gestor.turno.rotate(-3)
        gestor.procesar_apuesta((2, 'Tonto'))
        gestor._determinar_jugador_eliminado()

        # Jugador 5 no tiene dados, debe ser saltado
        assert gestor.turno[0] == 0