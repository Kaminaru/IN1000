from motorsykkel import Motorsykkel
# from motorsykkel import *  (importerer alt)

# prosedyre som lager 3 objekter med klassen Motorsykkel
def hovedprogram():
    mot1 = Motorsykkel("BMW","D21D13",120)    #opretter objekt av klassen Motorsykkel
    mot2 = Motorsykkel("Audi","G21S38",300)
    mot3 = Motorsykkel("Volvo","K54M42",1020)

    mot1.skrivUt()   # skriver ut objekts merke, registreringsnummer og en kilometerstand
    mot2.skrivUt()
    mot3.skrivUt()

    mot3.kjor(10)    # Legger til 10km til kilometerstand til objekt  mot3
    print(mot3.hentKilometerstand())  # skriver ut kilometerstand til objekt mot3

hovedprogram()
