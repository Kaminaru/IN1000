from hytte import Hytte
from tur import Tur

class Turplanlegger:
    def __init__(self,filnavn1,filnavn2):
        a = self._hytterFraFil(filnavn1)  # ordbok med alle hytter
        self._ordBok = a
        self._listeTur = self._turenFraFil(filnavn2) # liste


    def _hytterFraFil(self,filnavn):
        ordbok = {}
        fil = open(filnavn)
        for linje in fil:
            biter = linje.strip().split()
            navn = str(biter[0])
            antSenger = int(biter[1])
            pris = float(biter[2])
            ordbok[biter[0]] = Hytte(navn,antSenger,pris)
        fil.close()
        return ordbok

    def _turenFraFil(self,filnavn):  # returnerer liste med alle turer objekter
        listeRef = []
        fil = open(filnavn)
        line = fil.readline()
        while line:
            tekst = line.strip()
            biter = fil.readline().strip().split()
            line = fil.readline()
            liste = []
            for i in biter:
                liste.append(self._ordBok[i])
            listeRef.append(Tur(liste,tekst))
        fil.close()
        return listeRef

    def finnTurer(self,personer,maksBelop,maksDager):
        print("Alle turer som passer:")
        for tur in self._listeTur:
            if tur.sjekkPrisPlass(personer,maksBelop):
                if maksDager >= len(tur.antallDager()):
                    tur.skrivTur()
