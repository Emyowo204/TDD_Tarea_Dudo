from src.juego.cacho import Cacho

def test_mirar_cacho():
    valoresEsperado = ['As', 'Quina', 'As']
    cacho = Cacho(valoresEsperado)
    valores = cacho.mirar()
    # Los valores de los dados son los esperados
    assert valores == valoresEsperado

def test_agitar_cacho():
    cacho = Cacho()
    cacho.agitar()
    valores = cacho.mirar()
    # Los valores de los dados están dentro de la lista de pintas
    assert set(valores).issubset({'As', 'Tonto', 'Tren', 'Cuadra', 'Quina', 'Sexto'})

    # La cantidad de dados es la correcta
    assert len(valores) == 5

def test_quitar_dado():
    valoresTest = ['As', 'Quina', 'As']
    cacho = Cacho(valoresTest)
    cacho.quitar_dado()
    valores = cacho.mirar()
    # La cantidad de dados se resta correctamente
    assert len(valores) == (len(valoresTest)-1)

    cacho = Cacho([])
    cacho.quitar_dado()
    valores = cacho.mirar()
    # Evitar tener un número negativo de dados
    assert len(valores) == 0

def test_agregar_dado():
    valoresTest = ['As', 'Quina', 'As']
    cacho = Cacho(valoresTest)
    cacho.agregar_dado()
    valores = cacho.mirar()
    # La cantidad de dados se suma correctamente
    assert len(valores) == (len(valoresTest)+1)