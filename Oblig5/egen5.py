# Skriv en beregningsprogram for skreddere med en funksjon som leser inn en
# fil der hver linje beskriver et navn på et mål og selve målet i tommer.
# Bruk fil som heter egen5.txt og dens innhold
# La programmet legge disse målene i en ordbok med navn på målet som
# nøkkelverdi og returner ordboken. Lag deretter en prosedyre som tar imot
# en liste av mål og benytter seg av tommerTilCm som du skrev tidligere for
# å skrive ut målene i centimeter.

# hoved funksjon, alt startes fra den funksjon
def main():
    ordbok = fileOrd() # ord bok som lages fra fil "egen5.txt". Funksjon brukes for det
    listeNavn = []     # tomt liste med navn til mål
    listeTommer = []   # tomt liste med beregning verdi til mål
    for i in ordbok:   # for loopen som legger verdier og nøkelnavn fra ordbok i liste
        listeNavn.append(i)   # legger til navn av mål til listeNavn
        listeTommer.append(ordbok[i]) # legger antalltommer til listeTommer
    beregninger(listeNavn,listeTommer) # kaller for prosedyre som beregner målene i centimeter

# Prosedyre som beregner målene i centimeter. Deretter skriver dem ut
# Den prosedyre tar imot 2 parametre. En for navn og andre for tommer som skal konvergeres
def beregninger(listeNavn, listeTommer):
    for i in range(len(listeNavn)):
        print(listeNavn[i], tommerTilCm(listeTommer[i]),"cm")

# Funksjon som lager ordbok fra tekst fil, ord bok har nøkkel navn som string, og verdi som float
# Den funskjon returnerer ordbok
def fileOrd():
    min_fil = open("egen5.txt")  # åpner egen5.txt fil
    ordbok = {}    # tomt ordbok
    for linje in min_fil:   # for loopen som tar alle verdier i alle linjer i fil
        biter = linje.split()  # deler linje
        ordbok[biter[0]]=float(biter[1])   # og lagrer dem i ordbok.
    return ordbok

def tommerTilCm(antallTommer):
    assert(antallTommer) > 0, "Feil tommer storelse"  # sjekker om parameter større enn 0
    return antallTommer*2.54

main()
