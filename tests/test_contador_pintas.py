from src.juego.cacho import Cacho
from src.juego.contador_pintas import Contador_Pintas

def test_contar_pintas_del_cacho():
    valoresIniciales = ['As', 'Quina', 'As', 'Tonto', 'Tren']
    cacho = Cacho(valoresIniciales)
    valores = cacho.mirar()
    contador = Contador_Pintas()

    total = contador.contar_pintas(valores, 'Quina')
    # La cantidad de dados con la pinta especificada es correcta
    assert total == 3

    total = contador.contar_pintas(valores, 'As')
    # La cantidad de dados con la pinta As es correcta
    assert total == 2

    total = contador.contar_pintas_sinAs(valores, 'Quina')
    # La cantidad de dados con la pinta especificada, excluyendo al As como comodín es correcta
    assert total == 1


