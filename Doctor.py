class Doctor():
    def __init__(self):
        self._Tiempo=0
    @property
    def Tiempo(self):
        return self._Tiempo
    @Tiempo.setter
    def Tiempo(self,tiempo):
        self._Tiempo=self._Tiempo+tiempo

    def __gt__(self, other):#gt:mayor
        return self._Tiempo>other._Tiempo
    def __lt__(self, other):
        return self._Tiempo<other._Tiempo


