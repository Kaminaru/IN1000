class Hytte:
    def __init__(self,navn,antSenger,pris):
      self._navn = navn
      self._antSenger = antSenger
      self._pris = pris

    def hentNavn(self):
        return self._navn

    def totPris(self,personer):
        return self._pris*personer

    def sjekkPlass(self,personer):
        if personer <= self._antSenger:
            return True
        return False

    def __str__(self):
        return  "Navn: " + str(self._navn) + " Antall senger: " + str(self._antSenger) + " Pris: " + str(self._pris)
    #    return "Navn: %s, Antall senger: %s, Pris: %s" % (self._navn, self._antSenger, self._pris)

    def __eq__(self,andreObjekt):
        if andreObjekt.hentNavn() == self._navn:
            return True
        return False
