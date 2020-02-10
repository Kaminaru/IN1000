class Celle:
    def __init__(self):
        """
        Opretter celle med gitt satus
        """
        self._status = False  # levende(False) eller dod(True)

    def settDoed(self):
        """
        Metode som setter statusen til cellen til dode
        """
        self._status = False

    def settLevende(self):
        """
        Metode som setter statusen til cellen til levende
        """
        self._status = True

    def erLevende(self):
        """
        Metode som returnerer cellens status. True eller False
        """
        return self._status

    def hentStatusTegn(self):
        """
        Metode som returnerer en tegnerepresentasjon av celles status i tegning av brettet
        Dersom cellen er levende, skal det returnerers en "O", hvis den er dod saa "."
        """
        if self.erLevende():   # her bruker jeg metode som jeg laget for  (if True)
            return "\033[92mO\033[37m"    # legger til gronfarge
        return "."
