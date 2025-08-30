class Contador_Pintas:

    def contar_pintas(self, lista, pinta):
        cantidad = 0
        for valor in lista:
            if valor == pinta or valor == 'As':
                cantidad += 1
        return cantidad

    def contar_pintas_sinAs(self, lista, pinta):
        cantidad = 0
        for valor in lista:
            if valor == pinta:
                cantidad += 1
        return cantidad