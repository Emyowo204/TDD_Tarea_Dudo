from src.juego.cacho import Cacho

class Contador_Pintas:

    def contar_pintas(self, cacho, pinta):
        cantidad = 0
        for valor in cacho.mirar():
            if valor == pinta or valor == 'As':
                cantidad += 1
        return cantidad

    def contar_pintas_sinAs(self, cacho, pinta):
        cantidad = 0
        for valor in cacho.mirar():
            if valor == pinta:
                cantidad += 1
        return cantidad