class Person:

        def __init__(self,navn,alder):
            """
            Oppretter person med gitt navn, alder og tomt liste med person hobbyer
            """
            self._navn = navn
            self._alder = int(alder)
            self._hobbyer = []

        def leggTilHobby(self,string):
            """
            Metode som tar imot en tekststreng og legger den til i hobbyer-liste
            """
            self._hobbyer.append(string)

        def skrivHobbyer(self):
            """
            Metoden som skriver ut alle hobbyene etter hverandre paa en linje
            """
            setning = ""
            for i in range(len(self._hobbyer)):
                setning += self._hobbyer[i] + " "
            print("Hobbyene:", setning)

        def skrivUt(self):
            """
            Metode som skriver ut navn og alder, men ogsaa alle hobbyer
            """
            print("Navn:", self._navn, " Alder:", self._alder)
            self.skrivHobbyer()
