# Hoved funksjon, der startes alt.
def main():
    min_fil = open("temperatur.txt")  # åpner temperatur.txt fil
    liste = []    # tomt liste
    for linje in min_fil:   # for loopen som tar alle verdier i alle linjer i fil
        liste.append(int(linje))     # og lagrer dem i liste. Men også tar bort \n
    min_fil.close()
    print("Gjennomsnittet er: ", gjennom(liste)) # kaller for gjennomsnitt funksjon
                                                 # og bruker liste som parameter
# funksjon som bruker liste som parameter. Og beregner summen av alle tall i liste
# og returnerer gjennomsnitt av summen (dvs. delere sumen på lengde av liste)
def gjennom(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum/len(list)

main()
