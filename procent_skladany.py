kwota=int(input("Ile bierzesz kredytu: "))
print(f"kwota: {kwota} PLN")

czas=int(input("Na jak dlugo bierzesz: "))
print(f"czas: {czas} lata")

procent=int(input("Na jaki procent: "))
print(f"procent: {procent} %")

dlug=kwota*(1+procent/100)**czas
print(dlug)

#ile przyrasta kazdego roku odsetek
dane=[]
zysk=0
for i in range(czas):
    zysk=((kwota)*(procent/100))
    kwota+=zysk
    dane.append(kwota)

print(kwota)
print(dane)
