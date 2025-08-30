from src.juego.dado import Dado

def test_lanzar_dado():
    dado = Dado()
    valor = dado.lanzar()
    assert valor in ['As', 'Tonto', 'Tren', 'Cuadra', 'Quina', 'Sexto']