import random

class Model(object):
    #va a regolare tutto il comportamento del gioco
    def __init__(self):
        self._Nmax = 100
        self._Tmax = 6 #tentativi massimi
        self._T = self._Tmax
        self._segreto = None #Lo settiamo a none e poi le resettiamo appena avviamo il gioco

    def reset(self):
        self._segreto = random.randint(0,self._Nmax)
        self._T = self._Tmax #crea nuovo segreto e resettare numero di vite rimanent
        print(self._segreto)

    def play(self, tentativo):
        """Questo metodo riceve come argomento un valore intero che sarà il tentativo del giocatore e lo confronta con il segreto
        -1 : se il segreto è più piccolo del tentativo
        0 : se il tentativo è uguale al segreto
        1 : se il segreto è più grande del tentativo
        2 : se non ho più tentativi disponibili"""

        #Verifichiamo se ho ancora vite per giocare
        self._T -= 1

        if tentativo == self._segreto:
            return 0

        if self._T == 0:
            # allora non ho più vite return 2
            return 2

        elif tentativo > self._segreto:
            #tentativo utente più grande del segreto
            return -1

        else:
            #tentativo
            return 1
    @property
    def Nmax(self):
        return self._Nmax

    @property
    def Tmax(self):
        return self._Tmax

    @property
    def T(self):
        return  self._T

    @property
    def segreto(self):
        return self._segreto

if __name__ == "__main__":
    m = Model()
    m.reset()
    print(m.play(50))
    print(m.play(10))
    print(m.play(20))
    print(m.play(30))
    print(m.play(80))
    print(m.play(100))

