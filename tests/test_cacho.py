from src.juego.cacho import Cacho

def test_mirar_cacho():
    valoresEsperado = ['As', 'Quina', 'As']
    cacho = Cacho(valoresEsperado)
    valores = cacho.mirar()
    assert valores == valoresEsperado