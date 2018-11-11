class Detector(object):

    def __init__(self, own_signal):
        self.own_signal = own_signal
        #TODO: completar con la inicializacion de los parametros del objeto
        pass

    def detectar(self, signal):

        # if loop para ver si existe una señal (diferente a algo)
        if signal != 0:

        #señal tiene que venir de medio (haya o no blanco)
        #comparar señal con self._own_signal
            return self.own_signal != signal
        else:
            return False


        #TODO: Completar
        pass
