# 1.Er ikke helt lovlig, fordi hvis input er storre enn 10 saa skal det skje ingenting.
# 2.I print funksjon vil det komme feilmedling fordi vi prover aa lege sammen
# string and integer. For aa lose den problem maa vi skrive print(str(b) +"Hei!")
# Og for aa gjore enda bedre kan vi bruke else som skal ha egen print ogsa, for
# aa faa respons naar input tall er storre enn 10



a = input("Tast inn et heltall! ")
b = int(a)
if b < 10:
    print(b +"Hei!")
