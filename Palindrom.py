#kajak
#civic
#atokanapapanakota
#elfukladalkufle

slowo = input("Wpisz slowo: ")
czy_jest_palindromem = True

for i in range(len(slowo)):
    if (slowo[i] != slowo[-i -1]):
        czy_jest_palindromem  = False
        break
print(f"Palindrom:  {czy_jest_palindromem}")
if czy_jest_palindromem:
    print('TAK jest palindromem')
else:
    print('Nie, nie jest')

