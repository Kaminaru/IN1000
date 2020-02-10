# Program som tar brukers tall input og spører om flere input om input er ikke 0
# Den program også lagrer alle bruker tall input i en liste
# Deretter skriver program ut alle input. Regner og skriver ut summen og størst og minst tall.

# Bruker input som legger tall inn i liste. Også while loopen for å kjøre før input skal bli lik 0
# Jeg må skrive input 1 gang før loopen for å gi verdig til variabel svar for at while skal ha
# noen ting for å starte fra.
svar = int(input("Skriv inn tall: "))
liste = []
while svar != 0:
    liste.append(svar)
    svar = int(input("Skriv inn tall: "))

# for loopen som går gjennom hele liste og skriver ut alt ut, på hver sin rad.
for i in liste:
    print(i)

# for loopen som regner og printer ut summen.
minSum = 0
for i in range(len(liste)):
    minSum += liste[i]
print("Summen er:", minSum)

# for loopen som sjekker størst tall i liste. Først skrevet jeg variabel for størst tall
# som blir endret etter for loopen skal finne tall som er større enn storstTall variablen
storstTall = liste[0]
for i in range(len(liste)):
    if liste[i] > storstTall:
        storstTall = liste[i]
print("Storst tall er:", storstTall)

# for loopen som sjekker for minst tall i liste. Fungere samme som den forige for loopen
# men motsatt vei.
minstTall = liste[0]
for i in range(len(liste)):
    if liste[i] < minstTall:
        minstTall = liste[i]
print("Minst tall er:", minstTall)

# Størst tall og minst tall jeg kunne finne med å bruke sort() funksjon, som kunne
# bli mye kortere men jeg valgt å gjøre annerledes.
