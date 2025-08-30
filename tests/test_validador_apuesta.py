from src.juego.validador_apuesta import Validador_Apuesta

def test_validar_apuesta_comun():
    val = Validador_Apuesta()

    apuestaIniNum = 3
    apuestaIniPin ='Tren'

    # La apuesta tiene un número mayor y misma pinta, es correcta
    assert val.validar(apuestaIniNum, apuestaIniPin, 5, 'Tren')
    # La apuesta tiene una pinta mayor y mismo número, es correcta
    assert val.validar(apuestaIniNum, apuestaIniPin, 3, 'Quina')
    # La apuesta tiene un número y pinta mayor, es correcta
    assert val.validar(apuestaIniNum, apuestaIniPin, 4, 'Cuadra')
    # La apuesta tiene un número mayor y menor pinta, es correcta
    assert val.validar(apuestaIniNum, apuestaIniPin, 4, 'Tonto')

    # La apuesta tiene mismo número y misma pinta, es incorrecta
    assert not val.validar(apuestaIniNum, apuestaIniPin, 3, 'Tren')
    # La apuesta tiene un número menor y misma pinta, es incorrecta
    assert not val.validar(apuestaIniNum, apuestaIniPin, 2, 'Tren')
    # La apuesta tiene una pinta menor y mismo número, es incorrecta
    assert not val.validar(apuestaIniNum, apuestaIniPin, 3, 'Tonto')
    # La apuesta tiene un número y pinta menor, es incorrecta
    assert not val.validar(apuestaIniNum, apuestaIniPin, 2, 'Tonto')