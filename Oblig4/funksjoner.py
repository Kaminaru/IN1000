# den program skal addere 2 tall ogsaa skal sjekke om hvor mange ganger det kommer bestemt
# bokstav i bestemt teksten.

# Funksjon som faar to verdier og regner ut summen og returnere summen
def adder(tall1,tall2):
    return tall1+tall2

# Funksjon som tar to verdier. En av dem tekst og andre er bokstav.
# Deretter regner ut antal valgte "bokstaver" finnes det i teksten
def tellForekomst(minTekst, minBokstav):
    # sjekker hvor mange bokstaver finnes i tekst. Med funksjon count()
    return brukerTekst.count(minBokstav)

# Legger kaller funksjon adder 2 ganger og lager egen varabel for hver return
summ1 = adder(1,5)
summ2 = adder(4,7)
print("Resultat av den første summen er:", summ1, "Den andre er:", summ2)

# Bruker input av tekst og bokstav som onsket aa brukes i funksjon tellForekomst
brukerTekst = input("Skriv tekst: ")
brukerBokst = input("Skriv bokstav: ")

# print som kaller for funksjon med bruk av variabler fra for
print("Det er", tellForekomst(brukerTekst, brukerBokst) , brukerBokst, "i tekst")
