# Lag program som skal ha mulighet aa cryptere brukers input på nesten samme måtte som cæsarchiffer
# Dvs. hver bokstav i brukers input skal skiftes til noen andre bokstav med bestemt avstand
# For eksempel du kan lage cryptering som skal skifte hver bokstav til noen andre som har +3 plass i alphabet

# funskjon som skal spørre om bruker vil fortsette
def moreToDo():
    answer = (input("\nDo you want to do something else? ")).lower()
    if answer == "yes":
        start()

# Funksjon som crypterer bruker input
# Den funksjon tar brukers input og spliter den og setter inn i liste, der hverbokstav har egen index
# For loopen, i er alle bokstaver i textList liste
# Først finner den i(bokstav) i alpha og finner ut index av den i alpha
# Etter på setter newIndex verdi av den alpha bokstav index -5 (brukt - fordi med + det er mulig at den skal komme over grense av mulig index)
# Etter på legger den ny bokstav(som har index av gammel bokstav -5 i alphabet) i newText
# Og for loopen går gjennom hele textListe, skal den printe ut hele newText (som er incryptert tekst)
def incrypt():
    alpha = "A0z9B12x74vF uGtH?s:IrJpKD6EoLnMNlOkP!3wjQiRh6CSgTfU.emy8Vd,WcXbYaZq"
    textList = list(input("Write text that you want to incrypt:\n"))
    newText = "\n"
    for i in textList:
        index = alpha.find(i)
        newIndex = index - 5
        newText += alpha[newIndex]
    print(newText)
    moreToDo()

# Den funksjon decryptere og fungerer samme vei som i incrypt.
# Den funksjon skal skifte index av cryptert bokstav til +5
# Men vi kan ikke bruker +5 fordi det er mulig det kommer over index grense
# Eneste forskjell er at NewIndex verdi skal bli lik index verdig i alphabet - 63.
# Det er samme årsak som i incryp med index - 63 skal vi ikke få feil melding noen som "over index value".
def decrypt():
    alpha = "A0z9B12x74vF uGtH?s:IrJpKD6EoLnMNlOkP!3wjQiRh6CSgTfU.emy8Vd,WcXbYaZq"
    textList = list(input("Write text that you want to decrypt: \n"))
    newText = "\n"
    for i in textList:
        index = alpha.find(i)
        newIndex = index - 63
        newText += alpha[newIndex]
    print(newText)
    moreToDo()

# Den funksjon kjøres på start og hver gang når bruker velger å fortsette etter cryptering eller decryptering
# Den printer "menyen"
# og spørrer om brukers input. Fra brukers input velges det bestemt funksjon som skal kjøres
# Jeg brukt "try" for å bli sikkert at bruker skal skrive tall, og om det ble skrevet tall som finnes ikke
# eller bokstav så kommer det feil melding og funksjonen start() skal kjøres igjen
def start():
    try:
        print("""
    1. Incrypt text
    2. Decrypt text""")
        answer = int(input("\nWhat would you like to do next? (number) "))
        if answer == 1:
            incrypt()
        elif answer == 2:
            decrypt()
        else:
            print("There is no number: ", answer)
            start()
    except ValueError:
        print("Try again")
        start()

print("\nWelcome to encryption program. \nWhat would you like to do?")
start()
