class Hund:

    def __init__(self,hundAlder, hundVekt):
        """
        Oppretter hund med gitt alder, vekt, metthet
        """
        self._alder = hundAlder
        self._vekt = hundVekt
        self._metthet = 10

    def hundAlder(self):
        """
        Metode som returnerer hund alder
        """
        return self._alder

    def hundVekt(self):
        """
        Metode som returnerer hund vekt
        """
        return self._vekt

    def spring(self):
        """
        Metode som skal minske metthet med 1, ogsaa vekt skal minske med 1
        om metthet er mindre enn 5
        """
        self._metthet -= 1
        if self._metthet < 5:
            self._vekt -= 1

    def spis(self,tall):
        """
        Metode som skal legge heltall(fra parameter) til metthet
        Hvis metthet er mer enn 7 saa vokser vekt med 1
        """
        self._metthet += int(tall)
        if self._metthet > 7:
            self._vekt += 1
