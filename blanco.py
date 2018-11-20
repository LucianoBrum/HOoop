"""
Un blanco que atraviesa un medio puede recibir una señal del radar y reflejarla, siendo detectado de esta manera
"""

import random

class Blanco(object):
    """
    Define un blanco a ser detectado por un radar
    """

    def __init__(self, amplitud, tiempo_inicial, tiempo_final):
        self.amplitud = amplitud
        self.tiempo_inicial = tiempo_inicial
        self.tiempo_final = tiempo_final

    def reflejar(self, señal, tiempo_inicial_detect, tiempo_final_detect):

        #si los tiempos de "existencia" del blanco están dentro de los tiempos de detección del radar, reflejar
        if tiempo_inicial_detect <= self.tiempo_inicial <= tiempo_final_detect \
            and tiempo_inicial_detect <= self.tiempo_final <= tiempo_final_detect:
            # modificar la señal que llega, modificando la amplitud según el parámetro propio del blanco
            # y cambiando la fase de manera arbitraria.
            # devolver señal modificada
            return [x + self.amplitud for x in señal[random.randint(1,50):]]
        else:
            return False


        #TODO ver como se encajan los tiempos del blanco y del intervalo de tiempo
        #(interseccion de invervalos)
        # despues aplicar los parametros del blanco sobre ese intervalo de tiempo
        #pass
        
