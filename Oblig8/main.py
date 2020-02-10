from regneklynge import Regneklynge
from rack import Rack
from node import Node

def main():
    abel = Regneklynge("regneklynge.txt") # lager ny Regneklynge objekt med filnavn parameter
    # printer 3 ganer antallNoder som har nok minne med bruk av noderMedNokMinne metode for regneklynge
    print("Noder med minst 32 GB:", abel.noderMedNokMinne(32))
    print("Noder med minst 64 GB:", abel.noderMedNokMinne(64))
    print("Noder med minst 127 GB:", abel.noderMedNokMinne(128))
    # skriver ut antall prosessorer i helle regneklynge
    print("Antall prosessorer:", abel.antProsessorer())
    # skrier ut antall rack i regneklynge (abel) objekt
    print("Antall rack:", abel.antRacks())


main()
