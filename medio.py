"""

Los medios albergan los blancos que reflejan las señales del radar

"""


class Medio(object):

    def __init__(self, blancos = 0):
        self.blancos = blancos


    def reflejar(self, una_senal, tiempo_inicial, tiempo_final):
        """
        Los blancos en el medio reflejan la señal
        """

        #el medio solo refleja si posee blancos dentro de él
        if self.blancos == 0:
            return False
        #si hay blancos, reflejar señal
        elif self.blancos != 0:
            #el blanco dentro del medio refleja la seña
            return self.blancos.reflejar(una_senal, tiempo_inicial, tiempo_final)
