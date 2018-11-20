import radar
import medio
import blanco
import generador
import detector
import math
import datetime

def main():

    # Intervalo de tiempo en el que vamos a medir
    tiempo_inicial = datetime.datetime(2016, 3, 5, 1)
    tiempo_final = datetime.datetime(2016, 3, 5, 10)

    # parametros del generador de senales
    amplitud = 0.2
    fase = 1
    frecuencia = 20*math.pi

    # construir un nuevo genrador de senales
    generador1 = generador.Generador(amplitud, fase, frecuencia)

    # construir un detector
    detector1 = detector.Detector()
    # establecer un umbral para la detección
    threshold = 0.01

    # construir un nuevo radar con su propio generador y detector
    radar1 = radar.Radar(generador1, detector1)

    # parametros para un blanco
    amplitud_de_frecuencia_del_blanco = amplitud * 0.06
    tiempo_inicial_del_blanco = datetime.datetime(2016, 3, 5, 2)
    tiempo_final_del_blanco = datetime.datetime(2016, 3, 5, 4)

    # construir un nuevo blanco con sus propios tiempos
    blanquito = blanco.Blanco(amplitud_de_frecuencia_del_blanco, tiempo_inicial_del_blanco, tiempo_final_del_blanco)

    # construir un medio que contenga el blanco previamente construido
    medium = medio.Medio(blanquito)

    # Hacer que el radar detecte si existe un blanco en el medio al que apunta.
    detected = radar1.detectar(medium, tiempo_inicial, tiempo_final, threshold)

    # si el radar detecta un blanco, imprime un mensaje y plotea las dos señales
    if detected:
        print('Target detected')
        radar1.plotear_señal(radar1.signal, radar1.reflected_signal)
    # si el radar no detecta un blanco, imprime un mensaje.
    else:
        print('No target detected')


if __name__ == "__main__":
    main()
