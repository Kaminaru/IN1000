# Main funksjon som innhlder den "start kode".
# Det er 9 assert uttrykk, 3 addisjon, subtraksjon og divisijon funksjoner
# Som sjekker om funksjon gir git svar. Hvis svar er ikke samme som ble gitt,
# Så stoppes program og skriver feil melding som ble skrevet som string i kode, dvs. "Feil"
def main():
    print("Summen er:", addisjon(2,5))
    assert(addisjon(2,5)) == 7, "Feil"
    assert(addisjon(2,-5)) == -3, "Feil"
    assert(addisjon(-2,-5)) == -7, "Feil"
    assert(subtraksjon(2,5)) == -3, "Feil"
    assert(subtraksjon(2,-5)) == 7, "Feil"
    assert(subtraksjon(-2,-5)) == 3, "Feil"
    assert(divisjon(2,5)) == 0.4, "Feil"
    assert(divisjon(2,-5)) == -0.4, "Feil"
    assert(divisjon(-2,-5)) == 0.4, "Feil"
    print("Tilsvarer:",tommerTilCm(4),"cm")  # sjekker om tommerTilCm funksjon fungerer
    skrivBeregninger()     # kaller for funksjon

# funksjon som adderer to parametre og returnerer svar.
def addisjon(par1,par2):
    return par1 + par2
# funksjon som trekker det andre parameteret fra det første
def subtraksjon(par1,par2):
    return par1-par2
# funksjon som delere den andre parameteret på den første
def divisjon(par1,par2):
    return par1/par2
# funskjon konverterer tommer til cm
def tommerTilCm(antallTommer):
    assert(antallTommer) > 0, "Feil tommer storelse"  # sjekker om parameter større enn 0
    return  antallTommer*2.54
# funksjon som tar brukers tall input og skriver ut svar til addering, subtraghering, og dividering
# etter på tar antal tommer som bruker input og skriver ut samme ting men i cm
def skrivBeregninger():
    print("\nUtregninger:")
    tall1 = float(input("Skriv inn tall 1: "))
    tall2 = float(input("Skriv inn tall 2: "))
    print("\nResultat av summering:", addisjon(tall1,tall2))
    print("Resultat av subtraksjon:", subtraksjon(tall1,tall2))
    print("Resultat av divisjon:", divisjon(tall1,tall2))
    print("\nKonverterning fra tommer til cm:")
    tommer = float(input("Skriv inn et tall: "))
    print("Resultat:", tommerTilCm(tommer))


# kaller den første funksjon
main()
