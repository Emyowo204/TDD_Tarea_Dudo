from src.juego.cacho import Cacho
from src.servicios.generador_aleatorio import generar_lista_aleatoria

class GestorPartida:
    VALORES_INICIALES = [1, 2, 3, 4, 5, 6]

    def __init__(self, num_jugadores):
        """
        Inicializa el gestor de partida con un número especificado de jugadores.
        :param num_jugadores: Número de jugadores en la partida.
        """
        if num_jugadores < 2 or not isinstance(num_jugadores, int):
            raise ValueError("Deben haber al menos dos jugadores.")
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
        En caso de empate, los jugadores empatados relanzan sus dados.
        """
        dados_iniciales = generar_lista_aleatoria(self.num_jugadores, 1, 6)
        self.turno_actual = self._determinar_jugador_inicial(dados_iniciales)

    @staticmethod
    def _determinar_jugador_inicial(dados):
        max_valor = max(dados)
        jugadores_max_valor = [i for i, valor in enumerate(dados) if valor == max_valor]
        # Si solo hay un jugador con el valor máximo, retorna su índice
        if len(jugadores_max_valor) == 1:
            return jugadores_max_valor[0]
        # Relanzar solo los empatados
        nuevos_dados = generar_lista_aleatoria(len(jugadores_max_valor), 1, 6)
        dados_empate = [0] * len(dados)
        for idx, jugador_idx in enumerate(jugadores_max_valor):
            dados_empate[jugador_idx] = nuevos_dados[idx]
        # Llamada recursiva solo con los nuevos valores de los empatados
        return GestorPartida._determinar_jugador_inicial(dados_empate)

    def avanzar_turno(self):
        """
        Avanza el turno al siguiente jugador en orden cíclico.
        """
        self.turno_actual = (self.turno_actual + 1) % self.num_jugadores

    def _convertir_a_diccionario(self):
        """
        Convierte la lista de jugadores a un diccionario para facilitar su manejo.
        :return: Diccionario con los jugadores y sus respectivos dados.
        """
        c1, c2, c3, c4, c5, c6 = 0, 0, 0, 0, 0, 0
        for jugador in self.jugadores:
            cacho = jugador.mirar()
            for i in range(len(cacho)):
                if cacho[i] is 1: c1+=1
                elif cacho[i] is 2: c2+=1
                elif cacho[i] is 3: c3+=1
                elif cacho[i] is 4: c4+=1
                elif cacho[i] is 5: c5+=1
                elif cacho[i] is 6: c6+=1
        return {1: c1, 2: c2, 3: c3, 4: c4, 5: c5, 6: c6}