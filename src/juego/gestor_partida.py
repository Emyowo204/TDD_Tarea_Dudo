from src.juego.cacho import Cacho
from src.servicios.generador_aleatorio import generar_lista_aleatoria

class GestorPartida:
    VALORES_INICIALES = [1, 2, 3, 4, 5, 6]

    def __init__(self, num_jugadores):
        """
        Inicializa el gestor de partida con un número especificado de jugadores.
        :param num_jugadores: Número de jugadores en la partida.
        """
        self.turno_actual = None
        self.num_jugadores = num_jugadores
        self.jugadores = [self.inicializar_jugadores() for _ in range(num_jugadores)]

    def inicializar_jugadores(self):
        """
        Inicializa un jugador con un cacho.
        :return: Un objeto Cacho con valores iniciales agitados.
        """
        cacho = Cacho(self.VALORES_INICIALES)
        cacho.agitar()
        return cacho
            
    def iniciar_partida(self):
        """
        Inicia la partida determinando el turno del primer jugador.
        El jugador con el dado más alto comienza.
        """
        dados_iniciales = generar_lista_aleatoria(self.num_jugadores, 1, 6)
        self.turno_actual = dados_iniciales.index(max(dados_iniciales))