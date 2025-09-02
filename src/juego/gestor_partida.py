from src.juego.cacho import Cacho
from src.juego.validador_apuesta import Validador_Apuesta
from src.servicios.generador_aleatorio import generar_lista_aleatoria
from src.juego.arbitro_ronda import ArbitroRonda

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
        self.apuesta_actual = (0, None)  # Apuesta inicial por defecto
        self.validador = Validador_Apuesta()
        self.arbitro = ArbitroRonda()

    __pintas = ['As', 'Tonto', 'Tren', 'Cuadra', 'Quina', 'Sexto']

    def __convertir(self, pinta):
        numero = 0
        for i in range(len(self.__pintas)):
            if self.__pintas[i] == pinta:
                numero = i+1
        return numero

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
        if len(self.jugadores[self.turno_actual].mirar()) == 0:
            self.avanzar_turno()

    def _convertir_a_diccionario(self):
        """
        Convierte la lista de jugadores a un diccionario para facilitar su manejo.
        :return: Diccionario con los jugadores y sus respectivos dados.
        """
        conteo = {i: 0 for i in range(1, 7)}
        for jugador in self.jugadores:
            for dado in jugador.mirar():
                if dado in conteo:
                    conteo[dado] += 1
        return conteo

    def procesar_apuesta(self, apuesta_nueva):
        """
        Procesa una nueva apuesta, validándola contra la apuesta actual.
        Si la apuesta es válida, avanza el turno al siguiente jugador.
        :param apuesta_nueva: Tuple (número, pinta) de la nueva apuesta.
        :raises ValueError: Si la apuesta es inválida.
        """
        if self.validador.validar(self.apuesta_actual[0], self.apuesta_actual[1], apuesta_nueva[0], apuesta_nueva[1]):
            self.apuesta_actual = apuesta_nueva
            self.avanzar_turno()
        else:
            raise ValueError("Apuesta inválida.")

    def llamar_arbitro(self, motivo):
        """
        Llama al árbitro para resolver una duda o calzo.
        :param motivo: 'Duda' o 'calzo' indicando el motivo de la llamada.
        :raises ValueError: Si el motivo es inválido.
        """
        estado_cachos = self._convertir_a_diccionario()
        existe_jugador_con_un_dado = any(len(jugador.mirar()) == 1 for jugador in self.jugadores)

        if motivo == 'duda':
            self._resolver_duda(self.arbitro, estado_cachos, existe_jugador_con_un_dado)
        elif motivo == 'calzo':
            self._resolver_calzo(self.arbitro, estado_cachos, existe_jugador_con_un_dado)
        else:
            raise ValueError("Motivo inválido. Debe ser 'duda' o 'calzo'.")

        self.apuesta_actual = (0, None)

    def _resolver_duda(self, arbitro, estado_cachos, existe_jugador_con_un_dado):
        """
        Resuelve una duda llamando al árbitro y actualizando los dados de los jugadores según el resultado.
        :param arbitro: Instancia del árbitro para resolver la duda.
        :param estado_cachos: Diccionario con el conteo de dados.
        :param existe_jugador_con_un_dado: Booleano indicando si hay algún jugador con un solo dado.
        """
        if arbitro.resultado_duda(estado_cachos, self.__convertir(self.apuesta_actual[1]), self.apuesta_actual[0],
                                  existe_jugador_con_un_dado):
            self.jugadores[self.turno_actual - 1].quitar_dado()
        else:
            self.jugadores[self.turno_actual].quitar_dado()

    def _resolver_calzo(self, arbitro, estado_cachos, existe_jugador_con_un_dado):
        """
        Resuelve un calzo llamando al árbitro y actualizando los dados del jugador actual según el resultado.
        :param arbitro: Instancia del árbitro para resolver el calzo.
        :param estado_cachos: Diccionario con el conteo de dados.
        :param existe_jugador_con_un_dado: Booleano indicando si hay algún jugador con un solo dado.
        """
        if arbitro.resultado_calzo(estado_cachos, self.__convertir(self.apuesta_actual[1]), self.apuesta_actual[0],
                                   existe_jugador_con_un_dado):
            self.jugadores[self.turno_actual].agregar_dado()
        else:
            self.jugadores[self.turno_actual].quitar_dado()