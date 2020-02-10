# Program bestaar av prosedyre som har 2 varaibler med bruker input, "navn" og
# "sted". Og print funksjon som printer tekst med bruk av 2 variabler nevnt for.
# Nede i programmet kalt jeg prosedyre "hilsen" 3 ganger. Saa den gjenta seg 3 ganger.

def hilsen():                        # Start av prosedyre "hilsen"
    navn = input("Skriv inn navn: ")
    sted = input("Hvor kommer du fra? ")
    print("Hei, " + navn + "! Du er fra " + sted + ".")

hilsen()                            # Her kaller vi prosedyre 3 ganger. Dvs. alt
hilsen()                            # som er i prosedyre skal gjentass flere 3 ganger.
hilsen()
