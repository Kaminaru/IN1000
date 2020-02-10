# Programm som skal legge til tall i liste og printe tredje og forste eliment i liste
# Den ogsaa skal ha nanv liste og mulighet aa legge til navn fra brukers input
# Andre delen av program skal sjekke om det finnes bestemt navn i liste.
# Den tredje del skal lage liste og legge til liste numbers og names sammen og printe dem. Og etter paa slette 2 site verdier i liste

numbers = [1,2,3]  # liste med tall
numbers.append(4)  # Legger til tall på slutt av number liste
print(numbers[0],numbers[2])  # Skriver ut første og tredje element i liste

# Funksjon som legger til input i liste "names"
def nameAsk():
    names.append(input("Skriv navn: "))

names = []                # tom liste
for i in range(4):        # kjører funksjon nameAsk() 4 ganger
  nameAsk()

# Variabel med tall som har int verdi, etter hvor mange "Daniel" eller "daniel"
# finnes i liste "names"
nameNumber = names.count("Daniel") or names.count("daniel")
if nameNumber == 0:                # Hvis den variabel lik 0 saa betyr det at det finnes ikke noen navn "daniel"
    print("Glemte du meg?")        # Saa printer det den
else:
    print("Du husket meg!")        # Hvis nameNumber => 1 saa skrives det

numbers_names = numbers + names    # Lager ny liste med aa lege liste numbers og names sammen
print(numbers_names)               # Printer ny liste
numbers_names.pop()                # Tar bort siste element fra liste
numbers_names.pop()
print(numbers_names)               # Printes liste etter 2 siste elementer slettes
