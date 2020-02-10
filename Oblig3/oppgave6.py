# Restaurant bestilings program.
# Lag program som har ordbok med flere argumenter for navn til rett, som har liste med priser.
# Program må ha bruker input for mat bestiling, også det må bli mulighet å bestile flere retter
# På slutt må program skrive ut alt som ble bestilt og skrive summen av alle rettene.

# Viktigst at program skal bli laget riktig vei, at det skal bli lett å utvikle den etter på.
# Eller lett å legge til flere retter og priser uten å endre andre deler av kode.
import random           # importerer random
order = {}              # tomt ordbok for bestilte retter
# Ordbok med alle retter og priser for, litten, medium og stor størelse
menyDi = {"Kebab": [35,55,70],
          "Pizza": [115,155,215],
          "Ramen": [65,80,100],
          "Drink": [25,30,35],
          "Dessert": [55,65,80]}

# funksjon som skriver menyen om bruker vil det
def menyShow():
    print("- This is what we have in meny:")
    for key in menyDi:   # for loopen som går gjennom ordbok menyDi og skriver ut alle argumenter
        print(key)

# funksjon som skriver ut alt som ble bestilt og hele prisen for alle retter
def fullPrice():
    together = 0
    print("\n----------------------------------------")
    print("Your orded:")
    for key in order:
        print(key, ":", order[key], "kr")
        together += order[key]
    print("In total it will cost:", together, "kr")
    print("------------------------------------------")

# Den variabel er veldig viktig for å få mulighet å bestille flere samme retter
# Fordi uten den hvis bruker velger samme rett, skal den ha samme argument, så den skal endre
# den gammel verdi. Men nå jeg legger ranNumber tall før argument.
# Så nå alle argumentene i ny ordbok er forskjelige. Som gjør mulig å bestile flere samme reter som har samme navn i gammel ordbok
ranNumber = 0
# funksjon som tar verdi av bestilt rett og spørrer om størrelse som ønskes. Og ut fra det skal det tas pris fra retter ordbok.
# etter på skal navn til bestilt rett og pris legges til ny ordbok for bestilt retter.
# På slutt av funksjon skal det også spørres om bruker ønsker å bestile enn til rett. Om bruker vil ikke så skal det kjøres fullPrice() funksjon
def orderSize(foodName):
    global ranNumber
    ranNumber += 1
    size = (input("Which size do you want to order?(Small/Medium/Big) ")).capitalize()
    if size == "Small":
        print("It will cost", menyDi[foodName][0], "kr")
# Som vi kan se brukt jeg (str(ranNumber) + "."+ foodName) for å legge tall til ny argument. Som gjør mulig å legge til flere samme retter i ny ordbok.
        order[str(ranNumber) + "."+ foodName] = menyDi[foodName][0]
    elif size == "Medium":
        print("It will cost", menyDi[foodName][1], "kr")
        order[str(ranNumber) + "." + foodName] = menyDi[foodName][1]
    elif size == "Big":
        print("It will cost", menyDi[foodName][2], "kr")
        order[str(ranNumber) + "." + foodName] = menyDi[foodName][2]
    else:
        print("Wrong size")
        orderSize(foodName)
# Hvis bruker vil bestille flere retter så skal kalles menyOrder() funksjon for å ta verdi av rett
# Hvis bruker vil ikke så skal det kjøres siste funksjon for beragning av pris.
    answer = input("Do you want order something else?(yes/no) ")
    if answer == "yes":
        menyOrder()
    elif answer == "no":
        fullPrice()
    else:
        print("Wrong answer")
        fullPrice()

# funksjon som spørrer om bestiling. Hvis den bestiling finnes i menyDi ordbok, så skal navn til rett kalles i orderSize(answer) som verdi: answer
def menyOrder():
    answer = (input("- What you want to order? ")).capitalize()
    if answer in menyDi:
        orderSize(answer)
    else:
        print("We have no", answer)
        menyOrder()

# Funksjon som spørrer om bruker vil se meny
def askMeny():
    answer = input("Do you want to see meny? ")
    answer = answer.lower()
    if answer == "yes":
        menyShow()
        menyOrder()
    elif answer == "no":
        menyOrder()
    else:
        print("Wrong input")
        askMeny()

# Start av program
print("Hello and wellcome to 5 star restaurant!")
askMeny()
