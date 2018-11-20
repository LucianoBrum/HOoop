"""

El detector es el encargado de comparar la señal que recibe del medio y determinar si existe un blanco

"""

class Detector(object):

    def __init__(self):
        pass

    def detectar(self, signal, own_signal, threshold):
        """
        comparar la señal que proviene del medio con la propia con un umbral determinado

        """

        # Comparar solo si existe una señal proveniente del medio
        if signal != False:
            # comparar fase y amplitud de las señales (teniendo en cuenta el umbral para esta última)
            if ((max(signal) - min(signal)) / 2) / ((max(own_signal) - min(own_signal)) / 2) > threshold \
                and signal.index(max(signal)) != own_signal.index(max(own_signal)):
                return True
        else:
            return False

