from hytte import Hytte

class Tur:
    def __init__(self, lisRef, tekst):
        self._lisRef = lisRef  # liste med alle objekter av hytter
        self._tekst = tekst  # beskrivelse av turen

    def skrivTur(self):
        print(self._tekst)
        for hytte in self._lisRef:
            print(hytte)

    def sjekkPrisPlass(self,personer,maksBelop):
        pris = 0
        for hytter in self._lisRef:
            pris += hytter.totPris(personer)
            if not hytter.sjekkPlass(personer):
                return False
        if pris > maksBelop:
            return False
        return True

    def antallDager(self):   # bruker den videre for aa hente antal ref for aa finne ut antall dager som trenges for den turen
        return self._lisRef
