# Skriv en klasse Person med en konstruktør som tar imot navn og alder. I
# tillegg skal konstruktoren ha en tom liste ​ hobbyer ​ . Skriv en metode ​
# leggTilHobby ​ som tar imot en tekststreng og legger den til i ​ hobbyer - ​
# listen. Skriv ogsaa en metode ​ skrivHobbyer . ​Denne metoden skal skrive alle
# hobbyene etter hverandre på en linje. Gi deretter Person-klassen en metode ​
# skrivUt ​ som i tillegg til å skrive ut navn og alder kaller paa metoden ​
# skrivHobbyer . ​ La brukeren skrive inn navn og alder, og lag et Person-objekt
# med informasjonen du faar. Deretter skal brukeren ved hjelp av en lokke faa
# legge til saa mange hobbyer de vil. Naar brukeren ikke lenger onsker aa oppgi
# hobbyer skal statistikk om brukeren skrives ut.

from person import Person


def hovedprogram():
    person1 = Person(input("Skriv navn: "), int(input("Skriv alder: "))) # sporer om navn og alder, og lager objekt fra det med classe Person
    svar = (input("Vil du legge hobbyene? ")).lower() # sporer om bruker vil adde hobbyene til person
    while svar == "ja":  # hvis ja, saa skal det kjores leggtilHobby metode som skal legge til hobby in i liste
        person1.leggTilHobby(input("Skriv hobby som du vil legge til: "))
        svar = (input("Vil du legge hobbyene? ")).lower()
    print("___________________________________________\n")
    person1.skrivUt()      # printer ut navn, alder og hobbyer til person
    print("___________________________________________")


hovedprogram()
