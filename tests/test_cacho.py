from src.juego.cacho import Cacho

def test_mirar_cacho():
    valoresEsperado = ['As', 'Quina', 'As']
    cacho = Cacho(valoresEsperado)
    valores = cacho.mirar()
    assert valores == valoresEsperado

def test_agitar_cacho():
    cacho = Cacho()
    cacho.agitar()
    valores = cacho.mirar()

    assert set(valores).issubset({'As', 'Tonto', 'Tren', 'Cuadra', 'Quina', 'Sexto'})
    assert len(valores) == 5