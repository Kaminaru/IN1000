# Program som lar bruker legge planer for en reise, med hjelp av nostet lister
# Og etter paa med index input velge bestem index i nostet liste.

# Tre lister. Der legges alle bruker input.
steder = []
klesplagg = []
avreisedatoer = []
reiseplan = [steder,klesplagg,avreisedatoer]
# 3 forskjelige bruker input som gjentas 5 ganger og legges til hver sin liste
for i in range(5):
    steder.append(input("Legg til reisemaal: "))
    klesplagg.append(input("Skriv inn klesplagg: "))
    avreisedatoer.append(int(input("Skriv dato: (eks.: 021828): ")))

# for-lokke for aa skrive ut innholdet i reiseplan.
for i in range(len(reiseplan)):
    print(reiseplan[i])

# La brukeren skrive index til reiseplan, og index til nostet liste in reiseplan.
# Skriver ut elementene paa oppgitte index eller skriver "ugyldig input" om det er index som finnes ikke
def brukerInput():
    i1 = int(input("Skriv inn index til det du vil velge i reiseplan:\n"))
    i2 = int(input("Skriv inn index til den delen av valgt reiseplan:\n"))

# Her den sjekker om index liste er storre eller lik av brukers input - 1
# -1 fordi, legnde av liste f.eks. kan bli 3, men maks mulig index nummer i den er lik 2
# Ogsaa skrevet jeg at brukers input maa bli storre eller lik 0. Det staar i oppgave at gildig input er >=0
    if (i1 <= (len(reiseplan)-1) and i1 >= 0) and (i2 <= (len(reiseplan[i1])-1) and i2 >= 0):
        print(reiseplan[i1][i2])
    else:
        print("Ugyldig input!")
        brukerInput()

brukerInput()
