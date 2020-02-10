import random
from celle import Celle

class Spillbrett:
    def __init__(self,rader,kolonner):
        """
        Opretter spillbrett med gitt dimensjoner. Lager nostet liste av gitt deminsojer
        I hver index av nostet liste lages det celle objekt. Som skal endres etter paa.
        """
        self._rader = int(rader)
        self._kolonner = int(kolonner)
        self._generasjoNmr = 0          # generasjon nummer
        self._todimList = []            # nosted liste
        for i in range(self._rader):
            list = []                   # liste som skal leges til nostetliste flere ganger
            for a in range(self._kolonner):
                # celle Navn skal endres for hver loopen av for, brukes for aa lage unik navn til celle
                celleNavn = "celle" + str(i) + str(a)   # navn til celle som laget av str1 og str2 nummer   *************
                celleNavn = Celle()         # ny celle objekt oprettes
                list.append(celleNavn)      # og legges in i liste
            self._todimList.append(list)    # den liste av den rad med saa mange celler som kolloner i spillebrett
                                            # leges til nosted liste.
        self.generer()                # genererer spillebrett
        self.tegnBrett()              # tegner spillebrett


    def tegnBrett(self):
        """
        Metode som skriver ut (tegner) spillebrett. Med bruk av for loopen og
        hentStatusTegn metode (som returnerer tegning av dod eller levende celle)
        """

        for i in range(5):         # for i range 5: 0-4
            print(" ")             # 5 blanke linjer

        for rad in self._todimList:   # nosted liste for loopen som gaar gjennom alle indexer i nostedliste
            for objekt in rad:
                print(objekt.hentStatusTegn(), end = "")  # tegner tegning for hver celle objekt i nostetliste
            print("")   # brukes for aa lage \n etter hver rad.

    def hentGenerasjon(self):
        """
        Metode som returnerer generasjons nummer.
        """
        return self._generasjoNmr


    def oppdatering(self):
        """
        Metode som lager 2 listen for hver dode celle som skal faa statsu levende
        og for alle levende celler som skal faa statsu dode
        Deretter med bruk av de 2 lister endrer den status til alle celler som ma ha status
        endring, med bruk av settLevende og settDoed metoder fra Celle class
        """
        listDode = []        # liste av alle dode celler som skal faa status levende
        listLevende = []     # liste av alle levende celler som skal faa status dode
        for rad in self._todimList:
            for celle in rad:
                # self._todimList.index(rad) finner index til bestemt rad
                # rad.index(celle) finner index til bestemt kolonne
                # dvs. jeg bruker det for aa fine index til bestemt celle objekt i nosted liste.
                # Det er fordi i for loopen jeg brukt ikke "in range()" funksjon derfor jeg maa fine index selv.
                antallNaboList = self.finnNabo(self._todimList.index(rad),rad.index(celle))  # brukes finnNabo metode for aa lage liste med nabo celler
                antallLevendeNabo = 0
                # for loopen som med bruk av antallNaboList liste skal finne antall levende n@r bestemt celle
                for i in antallNaboList:
                    if i.erLevende():  # hvis true
                        antallLevendeNabo += 1
                # if settning som sjekker om skal celle do eller leve avhenging av de naboe celler
                if celle.erLevende():    # hvis celle er levende fra for   (hvis true)
                    if antallLevendeNabo < 2 or antallLevendeNabo > 3:  # hvis antal levende nabo er mindre enn 2 eller storre enn 3 saa dor celle ette pa
                        listLevende.append(celle)   # legger celle objekt i liste for aa bli endret seinere
                elif not celle.erLevende():   # hvis celle er dode fra for
                    if antallLevendeNabo == 3:     # hvis antall levende nabo n@r bestem celle er lik 3 sa dode celle skal komme i livet
                        listDode.append(celle)    # legger celle objekt i liste for aa bli endret seinere
        # for loopen som endrer alt i listDode og listLevende lister til levende eller dode
        for a in listDode:
            a.settLevende()
        for a in listLevende:
            a.settDoed()
        self._generasjoNmr += 1    # legger til generasjons nummer



    def finnAntallLevende(self):
        """
        Metode utregner og returnerer antallLevende i hele spillebrettet
        """
        antallLevende = 0
        for i in self._todimList:  # for loopen som gaar gjennom alle indexer i nosted liste og legger til +1 til variabel for hver levende celle
            for a in i:            # og legger til +1 til variabel for hver levende celle
                if a.erLevende():  # hvis celle objekt er levende:  (if True)
                    antallLevende += 1     # antallLevende +1
        return antallLevende           # returnerer antall levende i helle spillebrettet


    def generer(self):
        """
        Metoden gaar gjennom rutenettet og sorger for at et tilfeldig
        antall celler faar statsus "levende"
        """
        for rad in self._todimList: # for loopen for nosted liste
            for celle in rad:
                if random.randint(0,2) == 2:    # hvis tilfeldig tall er 2  (fra 0,1,2 dvs.1/3)
                    celle.settLevende()   # saa den celle objekt er levende
                # trenger ikke gjore noen mer for de som er allerede er dode, fordi alle ny celle objekter er allerde har "dode" status

    def finnNabo(self,x,y):
        """
        Metode som finner alle nabo celler for gitt celle objekt bed bestemte x og y kordinater
        I vaar tilfelle det er index til celle objekt i nosted liste.
        """
        liste = []    # liste med alle nabo celler
        for a in range(-1,2):   # -1,0,1    a brukes som x (rader)
            for b in range(-1,2):   # -1,0,1   b brukes som y (kolonner)
                if (x+a) in range(0,len(self._todimList)) and (y+b) in range(0,len(self._todimList[x+a])):  # hvis x+a er ikke i spillebrett omrode og y+b ogsa sa gaar det videre til neste for setning
                    if (x+a != x) or (y+b != y):  # tar bort valgt celle kordinater. Dvs. kordinater til celle som ble kalt i metode kall med (x,y) skal ikke appendes. Fordi vi maa ha bare de som er n@r den celle
                        liste.append(self._todimList[x+a][y+b])   # legger til celle objekt i liste.
        return(liste)
