# Den program tar brukers input. Hvis bruker skriver "ja", saa faar han en svar
# hvis bruker skriver "nei" saa faar han en andre svar. Hvis bruker skriver
# ingenting eller andre ting enn "ja" eller "nei" saa kommer den tredje bestemt
# svar

bruSvar = input("Vil du ha brus?(ja/nei): ")  # bruker input

if bruSvar == "ja":                         # start av if setting
    print("Her har du en brus!")            # printer bestemt svar hvis if stemmer
elif bruSvar == "nei":                      # else if settning som sjekker om input
    print("Den er grei.")                   # var "nei"
else:
    print("Det forstod jeg ikke helt")      # har den skal skrives ut hvis noen
                                            # andre enn "ja" eller "nei" skal
                                            # skrives i input
