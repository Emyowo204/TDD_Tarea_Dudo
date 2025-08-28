import random as rdm


def generar_numero_aleatorio(inicio: int, fin: int) -> int:
    """Genera un número aleatorio entre inicio y fin (inclusive).

    Args:
        inicio (int): El límite inferior del rango.
        fin (int): El límite superior del rango.

    Returns:
        int: Un número aleatorio entre inicio y fin.
    """
    return rdm.randint(inicio, fin)


def generar_lista_aleatoria(size: int, inicio: int, fin: int) -> list:
    """Genera una lista de números aleatorios.

    Args:
        size (int): El tamaño de la lista.
        inicio (int): El límite inferior del rango de números aleatorios.
        fin (int): El límite superior del rango de números aleatorios.

    Returns:
        list: Una lista de números aleatorios.
    """
    return [generar_numero_aleatorio(inicio, fin) for _ in range(size)]
