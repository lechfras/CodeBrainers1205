a =[ 1, 7, 7, 1, 16, 15, 20, 20, 25, 20]

duplicate_items = set()
uniqate_items = []
for x in a:
    if x not in duplicate_items:
        uniqate_items.append(x)
        duplicate_items.add(x)

#print(duplicate_items)
print(uniqate_items)
print(a)

unikaty=list(set(a))

#sprawdzenie ile razy dana zmienna wystepuje na liscie:
ile_razy=0
tylko_raz=[]
for i in range(len(unikaty)):
    for j in range(len(a)):
        if unikaty[i]==a[j]:
            print(unikaty[i])
            ile_razy+=1
    print(f"teraz jest zmienna: {unikaty[i]} która powtarza się:{ile_razy}")

    if ile_razy==1:
        tylko_raz.append(unikaty[i])
    ile_razy=0

print(tylko_raz)
