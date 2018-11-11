import radar
import medio
import blanco
import generador
import datetime
import detector


# DISCLAMER!!
# todo esta en castellano por razones didacticas
# pero DEBEN programar en INGLES
# uno nunca sabe quien puede leer su codigo

def main():

    # Intervalo de tiempo en el que vamos a medir
    tiempo_inicial = datetime.datetime(2016, 3, 5, 1)
    tiempo_final = datetime.datetime(2016, 3, 5, 10)

    import math
    # parametros del generador de senales
    amplitud = 0.2
    fase = 1
    frecuencia = 20*math.pi

    #TODO construir un nuevo genrador de senales
    generador1 = generador.Generador(amplitud, fase, frecuencia)
    #generar una señal
    sent_signal = generador1.generar(tiempo_inicial, tiempo_final)
    #print(generador1)
    #TODO construir un detector
    detector1 = detector.Detector(sent_signal)
    print(detector1)
    #TODO construir un nuevo radar
    pepino = radar.Radar(generador1, detector1)
    print(pepino.generador, pepino.detector, pepino)

    # parametros para un blanco
    amplitud_de_frecuencia_del_blanco = amplitud + 100
    tiempo_inicial_del_blanco = datetime.datetime(2016, 3, 5, 2)
    tiempo_final_del_blanco = datetime.datetime(2016, 3, 5, 4)
    #TODO contruir un nuevo blanco
    blanquito = blanco.Blanco(amplitud_de_frecuencia_del_blanco, tiempo_inicial_del_blanco, tiempo_final_del_blanco)
    print(blanquito)

    #TODO contruir un medio
    medium = medio.Medio(blanquito)
    print(medium)
    #TODO construir un radar (que se fije si detecto)

if __name__ == "__main__":
    main()
