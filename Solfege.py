solfege =['do', 're', 'mi', 'fa', 'so', 'la', 'ti', 'Do']



"""
#W przód
for i in range(0,len(solfege)-1,1):
    print(solfege[i])

i = 0
while i <= len(solfege):
    print(solfege[i])
    i += 1


#for i, solfege in  enumerate(solfege,1):
#    print(i, solfege)

#W tył:

for i in range(len(solfege)-1,0, -1):
    print(solfege[i])

i = len(solfege) - 1

while i >= 0:
    print(solfege[i])
    i -= 1

for i in range( len(solfege) - 1, -1, -1) :
    print(solfege[i])
# z numeracją
for i,v in reversed(list(enumerate(solfege))):
    print(i,v)

"""

print(solfege)
up_direction=solfege[::1]
print(up_direction)

reverse= solfege[::-1]
print(reverse)


C_dur=[solfege[0], solfege[2], solfege[4]]
D_mol=[solfege[1], solfege[3], solfege[5]]
G_dur=[solfege[1], solfege[4], solfege[6]]
A_mol=[solfege[0], solfege[2], solfege[5]]
print(C_dur)
c_dur=[0,2,4]
d_mol=[1, 3,5]
g_dur=[1, 4, 6]
a_mol=[0,2,5]

# Wlazl kotek na plotek
skoczny_kot=[4,2,2,3,1,1,0,2,4,0,2,4,4,2,2,3,0,1,0,2,0,0,2,0]
#

for i in range (len(skoczny_kot)):
    nuta=skoczny_kot[i]
    graj=solfege[nuta]
    print(graj)
