from src.juego.validador_apuesta import Validador_Apuesta

def test_validar_apuesta_comun_correcta():
    val = Validador_Apuesta()
    apuestaIniNum = 3
    apuestaIniPin = 'Tren'
    # La apuesta tiene un número mayor y misma pinta, es correcta
    assert val.validar(apuestaIniNum, apuestaIniPin, 5, 'Tren')
    # La apuesta tiene una pinta mayor y mismo número, es correcta
    assert val.validar(apuestaIniNum, apuestaIniPin, 3, 'Quina')
    # La apuesta tiene un número y pinta mayor, es correcta
    assert val.validar(apuestaIniNum, apuestaIniPin, 4, 'Cuadra')
    # La apuesta tiene un número mayor y menor pinta, es correcta
    assert val.validar(apuestaIniNum, apuestaIniPin, 4, 'Tonto')

def test_validar_apuesta_comun_incorrecta():
    val = Validador_Apuesta()
    apuestaIniNum = 3
    apuestaIniPin = 'Tren'
    # La apuesta tiene mismo número y misma pinta, es incorrecta
    assert not val.validar(apuestaIniNum, apuestaIniPin, 3, 'Tren')
    # La apuesta tiene un número menor y misma pinta, es incorrecta
    assert not val.validar(apuestaIniNum, apuestaIniPin, 2, 'Tren')
    # La apuesta tiene una pinta menor y mismo número, es incorrecta
    assert not val.validar(apuestaIniNum, apuestaIniPin, 3, 'Tonto')
    # La apuesta tiene un número y pinta menor, es incorrecta
    assert not val.validar(apuestaIniNum, apuestaIniPin, 2, 'Tonto')

def test_validar_apuesta_par_a_as():
    val = Validador_Apuesta()
    apuestaIniNum = 6
    apuestaIniPin = 'Tren'
    # La apuesta tiene un número menor a la mitad del inicial (par), es incorrecta
    assert not val.validar(apuestaIniNum, apuestaIniPin, 2, 'As')
    # La apuesta tiene un número igual a la mitad del inicial (par), es incorrecta
    assert not val.validar(apuestaIniNum, apuestaIniPin, 3, 'As')
    # La apuesta tiene un número mayor a la mitad del inicial (par), es correcta
    assert val.validar(apuestaIniNum, apuestaIniPin, 4, 'As')

def test_validar_apuesta_impar_a_as():
    val = Validador_Apuesta()
    apuestaIniNum = 7
    apuestaIniPin = 'Tren'
    # La apuesta tiene un número menor a la mitad del inicial (impar), es incorrecta
    assert not val.validar(apuestaIniNum, apuestaIniPin, 3, 'As')
    # La apuesta tiene un número mayor a la mitad del inicial (impar), es correcta
    assert val.validar(apuestaIniNum, apuestaIniPin, 4, 'As')

def test_validar_apuesta_de_as():
    val = Validador_Apuesta()
    apuestaIniNum = 3
    apuestaIniPin = 'As'
    # La apuesta tiene un número menor al doble del inicial con cambio de pinta, es incorrecta
    assert not val.validar(apuestaIniNum, apuestaIniPin, 5, 'Tren')
    # La apuesta tiene un número igual al doble del inicial con cambio de pinta, es incorrecta
    assert not val.validar(apuestaIniNum, apuestaIniPin, 6, 'Tren')
    # La apuesta tiene un número mayor al doble del inicial con cambio de pinta, es correcta
    assert val.validar(apuestaIniNum, apuestaIniPin, 7, 'Tren')

    # La apuesta tiene un número menor al inicial con al misma pinta, es incorrecta
    assert not val.validar(apuestaIniNum, apuestaIniPin, 3, 'As')
    # La apuesta tiene un número igual al inicial con al misma pinta, es incorrecta
    assert not val.validar(apuestaIniNum, apuestaIniPin, 3, 'As')
    # La apuesta tiene un número mayor al inicial con al misma pinta, es correcta
    assert val.validar(apuestaIniNum, apuestaIniPin, 4, 'As')

def test_validar_apuesta_no_iniciar_con_as():
    val = Validador_Apuesta()
    apuestaIniNum = 0
    apuestaIniPin = None

    # La apuesta inicial es incorrecta si contiene as
    assert not val.validar(apuestaIniNum, apuestaIniPin, 2, 'As')