# Hovedfunksjon der alt startes. Den innholder ordliste
def main():
    mineOrd = []
    svar = input("Hva vil du gjore naa? (i,u,s) ") # svar varaibel faar verdi
    while svar != "s":   # skal kjøres alltid før bruker skriver "s"
        if svar == "i":  # hvis svar er "i", så skal det tas bruker input to ganger og legge dem samme og legge dem til liste
            streng1 = input("Skriv forste streng her: ")
            streng2 = input("Skriv andre streng her: ")
            mineOrd.append(slaaSammen(streng1,streng2))
        elif svar == "u": # hvis u ble valgs, saa skrives ut hele liste. Hver index verdi skives ut på hver si linje
            skrivUt(mineOrd) # kalles prosedyren med liste som parameter
        else:
            print("Feil valg") # skriver ut det om bruker skriver noen andre enn i,u,s
        svar = input("Hva vil du gjore naa? (i,u,s) ")

# funskjon som tar to parametre (strenger) og legger dem sammen
def slaaSammen(par1,par2):
    return par1+par2

# prosedyre som tar liste som parameter og skriver ut hver element i listen på hver sin linje
def skrivUt(liste):
    for i in liste:
        print(i)


main()
