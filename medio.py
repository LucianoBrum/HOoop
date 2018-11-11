class Medio(object):

    def __init__(self, blancos):
        self.blancos = blancos


    def reflejar(self, una_senal, tiempo_inicial, tiempo_final):
        """
        Los blancos en el medio reflejan la senal
        """

        #TODO reflejar en un medio debe reflejar en todos los blancos de un medio
        #tiene que colectar la señal que refleja el blanco y mandarla.

        # lo de abajo no?
        #si hay blancos, reflejar señal (que tiene que ver el tiempo?)
        if self.blancos != 0:
            #reflejar señal (pedirle la función reflejar al blanco)
            signal_reflect = una_señal
        #y devolver la senal reflejada (atenuada o corrida)
        pass
        #si no hay blanco, devolver señal vacia o señal de sarasa.
