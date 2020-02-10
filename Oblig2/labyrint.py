# Skriv et program for "mini labyrint" spill. Krav til oppgave er at det maa brukes
# for det meste, bare det som vi lært i timene. Oppgave må inholde minst 3 forskjelige rom
# som man kan gå mellom.


# Her jeg tenkt å lage program som er lett til utvide, her jeg kan lege flere
# rom og gjøre den spill mye mer komplisert. For eksempel legge til "random incounters"

from random import randint
doorOneOpen = 0                 # Variable for å sjekke om døra er åpent

# Første roms funksjon. Nesten alle funksjoner til romene har samme kode og tankegang
# Først spører den om veien som bruker vi ønsker å gå. (Samme ting er i andre roms funksjoner)
# Den sjekker med if setting om bruker skrevet side som finnes. Hvis bruker skrevet feil
# Så skal det komme feilmeldig, og etter på skal det returneres back til start av funksjon
# Samme i alle roms funksjoner.
def room1():
    way = input("\033[1;36;36m(R~1) \033[1;37;37mSo where you want to go?(left,right,front,back): ")
    if way == "left" or way == "right" or way == "front" or way == "back":
# Hvis brukers input er passende så med if setninger sjekkes hvilken vei ble valgt
# Og fra den valg skal det komme spesielt lagt print eller andre handlinger
        if way == "left":
            print("\033[1;32;32mThere is only a big hadwritten number. Nothing more to look her.\033[1;37;37m")
            room1()
        elif way == "right":
# Hvis det velges høyre side så kan vi se at det kommer print og det kaller for rom4 funksjon
            print("You found a little door on right side, and you are going in.")
            room4()
        elif way == "front":
# Er ingenting i front side så kaller den answer1 funksjon for print som skriver ut
# at det er ingenting i den side. Så kalles det room1 funksjon. Dvs. kommer back til start av den funksjon.
            answer1(way)
            room1()
        elif way == "back":
# Printer beskrivelse av neste rom. Og kaller rom2 funksjon
            print("There is a little entery on that side. And you going in")
            print("In that room there is only one door with symbol on it")
            print("It's dark in here... And kind of cold...")
            room2()
    else:
# Det kommer hvis bruker skrevet feil ord i input (For rom valgt)
        writeCor(way)
        room1()


# Rom 2 har samme kode og tankegang som rom1, men med litt endringer
# Hvis bruker velger venstre side så skal det sjekkes om døren er åpent, dvs variabel
# doorOneOpen er lik 1.
# Hvis døren er åpent så har bruker mulighet å gå inn med å svare "yes" eller ikke gå inn med å svare "no"
# Om bruker velger "yes" så kalles rom3 funksjon med print med "win text".
# Om bruker svarer "no", så skal rom2 funksjon kalles (samme funksjon som vi er i nå)
def room2():
    way = input("\033[1;36;36m(R~2) \033[1;37;37mWhere you will go now? ")
    if way == "left" or way == "right" or way == "front" or way == "back":
        if way == "left":
            if doorOneOpen == 1:
                answerDoor = input("Door is open, would you like to go inside? (\033[31myes\033[37m/\033[32mno\033[37m) ")
                if answerDoor == "yes":
                    room3()
                elif answerDoor != "yes" or answerDoor == "no":
                    room2()
            else:
# Om variabel doorOneOpen lik 0 (hadde ikke noen endringer fra start) skal det komme melding
# om at døren er løst
                print("\033[95mDoor with a symbol, but it can't be opened at this moment!\033[37m")
                room2()
        elif way == "right":
            answer1(way)
            room2()
        elif way == "front":
# Om bruke velger front side så kommer han back til rom1
            print("There is a little entery on that side. And you going in")
            print("And you are back in the same place where you are started from")
            room1()
        elif way == "back":
            answer1(way)
            room2()
    else:
        writeCor(way)
        room2()


# Rom med print om at bruker vant spilt. Så etter den funksjon ble kalt og print
# blir skrevet så avslutes program
def room3():
    print("\033[1;36;36m\n          Congratulations! You made that to the end!\n")


# Funksjon for rom4 som har samme type av kode som rom1 med bare med 2 mulig
# valg av vei og 2 veier uten noen vei.
def room4():
    way = input("\033[1;36;36m(R~4) \033[1;37;37mSo where you want to go now? ")
    if way == "left" or way == "right" or way == "front" or way == "back":
        if way == "right":
            print("There is a door. So you going in")
            print("\033[95mIn this room you saw only one red buttom with black screen on the side\033[37m")
            room5()
        elif way == "left":
            print("There is a little door on left side, and you going in.")
            print("Looks like you are back in the same place where you are started from")
            room1()
        elif way == "front":
            answer1(way)
            room4()
        elif way == "back":
            answer1(way)
            room4()
    else:
        writeCor(way)
        room4()

# I den funksjon startes alt som i alle andre rom funksjoner.
def room5():
    way = input("\033[1;36;36m(R~5) \033[1;37;37mSo where would you go right now? ")
    if way == "left" or way == "right" or way == "front" or way == "back":
        if way == "left":
# Om bruker velger left så kommer det bak til rom4
            print("There is small entery. And you going in")
            print("Looks like you already been here...")
            room4()
        elif way == "right":
            answer1(way)
            room5()
        elif way == "front":
# Om bruker velger front side så kommer det print med beskrivelse av situasjon
# Hvis bruker velger "yes" så skal variabel "doorOneOpen" endres til 1
# Og det i min kode betyr at "døren i rom2 er åpent".
            print("\033[95mThere is a little red button that you saw before.")
            print("Looks like it have the same symbol that you saw on the door before\033[37m")
            answerButton = input("Would you press it? (\033[31myes\033[37m/\033[32mno\033[37m) ")
            if answerButton == "yes":
                global doorOneOpen # Forteller til funksjon at det skal brukes global variabel
# Før å endre variabel "doorOneOpen", skal det sjekkes om det ble endret før
# Og hvis den er endret før så skal det komme print om at "ingenting som skjer"
                if doorOneOpen == 1:
                    print("Looks like nothing changes...")
                elif doorOneOpen == 0:
                    print("It shows \033[1;31;31m'Door is opend'\033[1;37;37m")
                    print("On the black screen, after pressing button")
                    doorOneOpen = 1
                room5()
# Hvis bruker ønsker ikke trykke på knappen så skal det kalles samme funskon av rom5
# Dvs. det skal komme på start av samme rom.
            elif answerButton != "yes" or answerButton == "no":
                room5()
        elif way == "back":
            answer1(way)
            room5()
    else:
        writeCor(way)
        room5()


# Den funksjon kalles hver eneste gang når bruker velger side der det finnes ikke noen vei
# Det er på en måtte tilbake melding om at det er ingen vei videre, og man må velge andre veien
# Men for at det skal ikke bli alt for skjedelig med samme melding, skrevet jeg 3
# meldinger som velges tilfelding med if setning.
def answer1(side):
    tilfeldig = randint(1, 3)
    if tilfeldig == 1:
        print("\033[1;32;32mThere is nothing on " + side + " side...\033[1;37;37m")
    elif tilfeldig == 2:
        print("\033[1;32;32mLooks like it's just a wall on the " + side + " side.\033[1;37;37m")
    elif tilfeldig == 3:
        print("\033[1;32;32mThere is no where to go on the " + side + "side.\033[1;37;37m")

# Funksjon som kalles etter bruker skriver feil side i input.
def writeCor(word):
    print("\033[1;32;32m There is no such way as: " +
    "\033[1;31;31m" + word + ".\033[1;32;32m Please write correctly! \033[1;37;37m \n")

# Start av spill.
print("\n                 Hello. And wellcome to small maze game!")
print("In this game your character will always look in front(North) side. Let's begin!")
input("\033[1;32;32m                          Press" + "\033[1;31;31m ENTER" +
"\033[1;32;32m to start! \033[1;37;37m \n")

# Beskrivelse av første rom, skrevet den her og ikke i selve rom funksjon, for at
# den melding skal komme bare en gang
print("""You are in the big dark room with 2 doors on some sides of the room
and one big handwritten "R~1" on the wall.
Looks like this is a number of the room! Choose wisely where to go!""")
room1()   # kaller for funksjon av første rom
