# Programm med liste. Og med mulighet å legge til produkt og pris med hjelp av bruker input
# ordbok med varenanv som nøkkelverdier og varepriser som innholdsverdier
store = {"Melk": 14.90,
         "Brød": 24.90,
         "Yoghurt": 12.90,
         "Pizza": 39.90}
print(store)

# for, som kjører det som er inne i den 2 ganger
for i in range(2):
    try:   # prøver hvis den kan kjøres
        # Legger nøkkelverdier og innholdsverier i ordbok fra brukerinput
        # capitalize fuknsjon endrer første bokstav av input til stor bokstav
        store[(input("Skriv navn til produkt: ")).capitalize() ] = float(input("\nSkriv pris for produkt: "))
    except ValueError:   # hvis feilmelding er ValueError, så skipper den det som skjer nå
    # skriver print ut, og fortsetter å kjøre if loopen
        print("Skriv riktig pris!")
print(store)
