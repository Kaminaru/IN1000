# Program skal ta tall for farenheit og etter paa skrive den ut. Etter pa med bruk
# av liten bestemt utregning skal den utregne celsius fra tall i farenheit
# og etter paa skriver den ut.
fahr = int(input("Skriv fahrenheit tall: "))
print("Temperaturen i fahrenheit er: " + str(fahr))   # str komand brukes for aa
# endre int tall fra variable "fahr" til string for at vi kunne legge tekst og "tall" sammen
cels = float((fahr-32)*5/9)       # variabler med utregning for celsius fra gitt farenheit tall.
print("Temperaturen i celsius er: " + str(cels))
