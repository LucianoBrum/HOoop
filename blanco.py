class Blanco(object):
    """
    Define un blanco a ser detectado por un radar
    """

    def __init__(self, amplitud, tiempo_inicial, tiempo_final):
        self.amplitud = amplitud
        self.tiempo_inicial = tiempo_inicial
        self.tiempo_final = tiempo_final
        #TODO: completar con la inicializacion de los parametros del objeto
        pass

    def reflejar(self, senal, tiempo_inicial, tiempo_final):
        #tiempo durante el cual el blanco se está moviendo por el espacio, con sus propios tiempos
        detection_time = (self.tiempo_final - self.tiempo_inicial).seconds
        #tiempo durante el cual llega la señal del generador
        #radar_signal_time =
        # modificar la señal que llega, cambiarle de fase o amplitud.
        # devolver señal modificada


        #TODO ver como se encajan los tiempos del blanco y del intervalo de tiempo
        #(interseccion de invervalos)
        # despues aplicar los parametros del blanco sobre ese intervalo de tiempo
        pass
        
