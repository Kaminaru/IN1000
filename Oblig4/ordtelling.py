# Program som skal telle antall ord i tekst som ble skrevet i input.
# Program skal ogsaa skrive ut hvor ofte finnes samme ord i teksten og hvor mange
# bokstaver har hver bestemt ord

# variabel som brukes for aa telle hvor mange ord er i setning.
wordNumber = 0
# funksjon som tar ord og returnerer lenge av den ord
def ordBokstaver(ord):
    return len(ord)

# Funksjon som tar teksten og spliter den
# Etter paa legger alle nye ord i "ordbok" med ord som nokel ord og tall 1 som verdi
# Hvis det er allerede finnes nokel verdi med samme navn som ord saa legges det +1 til verdi
# Som gjor mulig aa regne antal samme ord i tekst
# Den funksjon returnerer ordbok i den global ordbok
def antalOrd(tekst):
    ordbok = {}
    tekst = tekst.lower()
    for i in tekst.split():
        global wordNumber
        wordNumber +=1
        if i in ordbok:
            ordbok[i] += 1
        else:
            ordbok[i] = 1
    return ordbok

# varaibel som lik return verdi av funksjon antalOrd.
# Dvs. etter bruker skriver tekst inn, skal funksjon antalOrd returnere ordbok
# med ord som har hver(unik) ord som nokkel ord og tall som verdi.
ordBok = antalOrd(input("Skriv en setning:\n"))

# Printer antall ord som ble skrevet i brukers tekst
print("Det er", wordNumber ,"ord i setningen din.")

# for loopen som gar gjennom ordBok og bruker informasjon fra den ordbok for aa
# skrive ut ord, antall ganger den kommet i teksten, og hvor mye bokstaver den ord har
for i in ordBok:
    print("Ordet:", "'", i , "'", "forekkommer", ordBok[i],
     "ganger, og har", ordBokstaver(i), "bokstav/er")
