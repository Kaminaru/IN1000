# Program med ordbok som har navn til brukere med verdier for hva brukere spiser

# Det er ordbok med verdier og argument
matplan = {"Kari Nordmann":["brød","egg","pølser"],
           "Kara Nordmann":["ost","egg","biff"]}

# Prosedyre som tar brukers input for navn og bruker den for aa sjekke om det finnes
# navn i ordbok matplan. Hvis det finnes ikke saa kommer det feil melding.
# Hvis det finnes saa tar det verdier i den "navn argument" og bruker dem i print
# Den print skriver ut hva de spiser for frokost, lunsj og middag
def matPlan():
    navn = input("Skriv navn til person: ")
    if navn in matplan:
        print(navn, "spiser", matplan[navn][0], "til frokost,", matplan[navn][1], "til lunsj og", matplan[navn][2], "til middag")
    else:
        print("Bruker er ikke registrert")


while True:            # while som skal kjøre matPlan funksjon heletiden
    matPlan()
