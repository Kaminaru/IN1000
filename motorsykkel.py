class Motorsykkel:
    def __init__(self,bilMerke,bilRegNum,avstand):
        """
        Oppretter motrsykkel med gitt merke, registreringsnummer og kilometerstand
        """
        self._merke = bilMerke
        self._regNum = bilRegNum
        self._avstand = avstand

    def kjor(self,km):
        """
        Avstand metoden som legger til antall km til avstand til motorsykkel
        """
        self._avstand += km


    def hentKilometerstand(self):
        """
        Metode som returnerer motosykkelens totale kilometerstand
        """
        return self._avstand


    def skrivUt(self):
        """
        Metode som skriver ut merke, registrerningsnummer og kilometerstand
        """
        print(self._merke, self._regNum, self._avstand)
