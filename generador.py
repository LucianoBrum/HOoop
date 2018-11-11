"""
Un generador de senal es el responsable de generar una senal portadora.

"""


class Generador(object):

    def __init__(self, amplitud, fase, frecuencia):
        self.amplitud = amplitud
        self.fase = fase
        self.frecuencia = frecuencia

        #  muestras por segundo
        self.frecuencia_muestreo = frecuencia*3


    def generar(self, tiempo_inicial, tiempo_final):

        import math
        import numpy as np

        cantidad_muestras = (tiempo_final - tiempo_inicial).seconds/\
        self.frecuencia_muestreo

        muestras = range(int(cantidad_muestras)) #hacerlo int para que sirva el range
        #TODO agregar un ruido blanco a la senal

        ret = [self.amplitud*math.sin(2*(1/self.frecuencia)*i+self.fase) \
                for i in muestras]

        #hacer ret array para poder usarlo en noise
        retarray = np.asarray(ret)
        #hacer el ruido para la función
        noise = np.random.normal(0, 0.01, retarray.shape)

        #devolver el array en forma de lista
        return (retarray + noise).tolist()


