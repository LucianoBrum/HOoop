"""
Un generador de señal es el responsable de generar una senal portadora.

"""
import math
import numpy as np


class Generador(object):

    def __init__(self, amplitud, fase, frecuencia):
        self.amplitud = amplitud
        self.fase = fase
        self.frecuencia = frecuencia

        #  muestras por segundo
        self.frecuencia_muestreo = frecuencia*3

    def generar(self, tiempo_inicial, tiempo_final):

        cantidad_muestras = (tiempo_final - tiempo_inicial).seconds/\
        self.frecuencia_muestreo

        #hacer entera la cantidad de muestras para poder utilizar range y luego generar señal.
        muestras = range(int(cantidad_muestras))

        #generar la señal limpia
        sig = [self.amplitud*math.sin(2*(1/self.frecuencia)*i+self.fase) \
                for i in muestras]

        #transformar la señal en un array de numpy
        retarray = np.asarray(sig)

        #generar el ruido para la señal
        noise = np.random.normal(0, 0.01, retarray.shape)

        #devolver la señal con el ruido incluido en forma de lista
        return (retarray + noise).tolist()


