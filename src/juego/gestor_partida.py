from src.juego.cacho import Cacho
from src.servicios.generador_aleatorio import generar_lista_aleatoria

class GestorPartida:
    def __init__(self, num_jugadores):
        self.turno_actual = None
        self.num_jugadores = num_jugadores
        self.jugadores = [None] * num_jugadores
        self.inicializar_jugadores()

    def inicializar_jugadores(self):
        for i in range(self.num_jugadores):
            self.jugadores[i] = Cacho()
            
    def iniciar_partida(self):
        dados_iniciales = generar_lista_aleatoria(self.num_jugadores, 1, 6)
        self.turno_actual = dados_iniciales.index(max(dados_iniciales))