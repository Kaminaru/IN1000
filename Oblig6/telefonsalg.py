# Program som tar inn data fra fil og skriver ut statistikk for et telefonsalg-firma
# For aa gjore dette, leser den inn tekst fra en fil som formatert slik at det er
# to ord paa hver linje, adskilt av et mellomrom, der er forste ordet er et navn og
# det andre ordet er et salgstall.


# prosedyre som kaler for funksjon innlesing med salgstall.txt fil navn som parameter
# for aa faa ordbok. Etter paa bruker den prosedyren ordbok for aa skrive bestemt tekster
# med bruk av andre funksjoner og prosedyrer.
def hovedprogram():
    ordbok = innlesing("salgstall.txt")
    maanedensSalgsperson(ordbok)
    print("Aktive selgere denne maaneded:", len(ordbok))
    print("Totalt antall salg:", totaltAntallSalg(ordbok))
    print("Gjennomsnittlig antall salg per salgsperson:", gjennomsnittSalg(ordbok))

# funksjon som tar filnavn som parameter. Denne funksjonen skal lese en fil ved
# hjelp av filnavn og legge alle linjene i filen inn i en ordbok, der den ansattes
# navn blir nokkelverdien og antallet salg blir innholdsverdien. Deretter
# returnerer funksjon den ordbok.
def innlesing(filnavn):
    min_fil = open(filnavn)  # åpner salgstall.txt fil
    ordbok = {}    # tomt ordbok
    for linje in min_fil:   # for loopen som tar alle verdier i alle linjer i fil
        biter = linje.split()  # deler linje
        ordbok[biter[0]]=int(biter[1])    # og lagrer dem i ordbok.
    min_fil.close()
    return ordbok

# prosedyre som tar imot en ordbok, gaar gjennom denne og skriver ut navn og
# antall salg for den personen som solgte mest den maaneden.
def maanedensSalgsperson(ordbok):
    maxSalg = 0
    maxSalgPerson = ""
    for i in ordbok:
        if ordbok[i] > maxSalg:
            maxSalg = ordbok[i]
            maxSalgPerson = i
    print("Maanedens ansatte er", maxSalgPerson, "med", maxSalg, "salg. \n")

# funksjon som tar imot ordbok, og returnerer summen av verdiene i ordboken
def totaltAntallSalg(ordbok):
    summen = 0
    for i in ordbok:
        summen += ordbok[i]
    return summen

# funksjon som tar imot en ordbok og returnerer gjennomsnittet av verdiene dens.
def gjennomsnittSalg(ordbok):
    return totaltAntallSalg(ordbok) / len(ordbok)

hovedprogram()
