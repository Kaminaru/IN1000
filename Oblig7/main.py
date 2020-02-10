from spillerbrett import Spillbrett


# prosedyre som sporrer bruker om rader og kolonner. Etter pa bruker det for aa lage spillebrettet
# Deretter tegnes spillebrett i konsollen. Bruker har mulighet a fortsette til neste generasjon
# med aa trykke Enter eller avslute program med a trykke q. Bruker ogsaa faar informasjon om generasjons tall
# og antall levende celler i spillebrett
def main():
    rader = int(input("Hvor mange rader du vil ha i spillebrettet? "))
    kolonner = int(input("Hvor mange kolonner du vil ha i spillebrettet? "))
    spilleb1 = Spillbrett(rader,kolonner)   # lager Spillbrett objekt

    print("Generasjon:", spilleb1.hentGenerasjon(), "- Antall levende celler:", spilleb1.finnAntallLevende())  # skriver ut generasjon nummer og antall levende celler
    svar = input("Press enter for aa fortsette. Skriv inn q og trykk enter for aa avslutte: ")
    while svar != "q":   # while loopen som avslutes bare naar brukers input er lik "q"
        spilleb1.oppdatering()    # kaller for oppdaterings metode for spillbrett objekt
        spilleb1.tegnBrett()     # kaller for tegnBrett metode for spillbrett objekt
        print("Generasjon:", spilleb1.hentGenerasjon(), "- Antall levende celler:", spilleb1.finnAntallLevende())
        svar = input("Press enter for aa fortsette. Skriv inn q og trykk enter for aa avslutte: ")


main()
