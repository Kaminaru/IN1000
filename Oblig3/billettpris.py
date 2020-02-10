# Program som beregner billettpris avhening av kjøperens alder.

# Funksjon som beregner billettpris
def information():
    alder = int(input("Skriv din alder her: "))     # Bruker input for alder
    billettpris = 0      # bilettpris variabler som lagrer pris

    if alder <= 17:
        billettpris =+ 30
    elif alder > 17 # and alder < 63:
        billettpris =+ 50
    elif alder >= 63:
        billettpris =+ 35
    print("Billett pris for din alder er: " + str(billettpris))
# Det er problemet med prosedyre i linje 10. Hvis bruker skirver alder mer enn 17
# Så skal program velge linje 10-11 og droppe linje 12 og 13
# Men det er mulig å forbedre den if settning med å legge til "and alder < 63" i linje 10
# Det skal gjøre at alder som er mer enn 63 skal ikke aksepteres i linje 10 og skal gå videre
# til linje 12. Og det er det vi treneger.


# for loopen som kjører samme komand 4 ganger
for x in range(4):
    information()
