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

def test_quitar_dado():
    valoresTest = ['As', 'Quina', 'As']
    cacho = Cacho(valoresTest)
    cacho.quitar_dado()

    assert len(cacho.mirar) == (len(valoresTest)-1)

    valoresTest = []
    cacho = Cacho(valoresTest)
    cacho.quitar_dado()

    assert len(cacho.mirar) == 0