"""
El radar es el encargado de generar una señal con su generador y detectar la existencia de blancos en el medio
al que apunta
"""
import matplotlib.pyplot as plt

class Radar(object):

    def __init__(self, generador, detector):
        self.generador = generador
        self.detector = detector
        self.signal = False
        self.detected_signal = False

    def detectar(self, medio, tiempo_inicial, tiempo_final, threshold):

        """
        Detecta si hay un blanco en un medio, en un intervalo de tiempo.
        """
        # El generador propio del radar genera una señal.
        self.signal = self.generador.generar(tiempo_inicial, tiempo_final)

        # La señal se refleja (o no) en el medio al que el radar apunta
        self.reflected_signal = medio.reflejar(self.signal, tiempo_inicial, tiempo_final)

        # El detector propio del radar recibe la señal reflejada y la compara con la señal enviada
        # para saber si existe un blanco
        return self.detector.detectar(self.reflected_signal, self.signal, threshold)

    def plotear_señal(self, own_signal, signal):
        plt.plot(own_signal, color = 'blue', label= 'señal propia')
        plt.plot(signal, color = 'red', label= 'señal detectada')
        plt.legend(loc='upper right')
        plt.show()
