from src.juego.cacho import Cacho
from src.juego.contador_pintas import Contador_Pintas

def test_contar_pintas_del_cacho():
    valoresIniciales = ['As', 'Quina', 'As', 'Tonto', 'Tren']
    cacho = Cacho(valoresIniciales)
    contador = Contador_Pintas()

    total = contador.contar_pintas(cacho, 'Quina')
    # La cantidad de dados con la pinta especificada es correcta
    assert total == 3

    total = contador.contar_pintas(cacho, 'As')
    # La cantidad de dados con la pinta As es correcta
    assert total == 2

    total = contador.contar_pintas_sinAs(cacho, 'Quina')
    # La cantidad de dados con la pinta especificada, excluyendo al As como comodín es correcta
    assert total == 1

def test_contar_pintas_totales():
    cacho1 = Cacho(['As', 'Quina', 'As', 'Tonto', 'Tren'])
    cacho2 = Cacho(['Sexto', 'As', 'Tren', 'Tonto', 'Cuadra'])
    cacho3 = Cacho(['Quina', 'Sexto', 'Cuadra', 'As', 'Quina'])

    cachosEnJuego = [cacho1, cacho2, cacho3]
    contador = Contador_Pintas()

    total = contador.contar_pintas_totales(cachosEnJuego, 'Quina')
    # La cantidad de dados con la pinta especificada en el juego es correcta
    assert total == 7

    total = contador.contar_pintas_totales(cachosEnJuego, 'As')
    # La cantidad de dados con la pinta As en el juego es correcta
    assert total == 4

    total = contador.contar_pintas_totales_sinAs(cachosEnJuego, 'Quina')
    # La cantidad de dados con la pinta especificada en el juego, excluyendo al As como comodín es correcta
    assert total == 3
