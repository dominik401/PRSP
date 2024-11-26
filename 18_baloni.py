b, p = map(int, input("unesi broj balona i prijatelja: ").split())
boje = input()

kolekcija = {}

for boja in boje:
    if boja in kolekcija:
        kolekcija[boja] += 1
    else:
        kolekcija[boja] = 1

raspodjela = True

for broj_boja in kolekcija.values():
    if broj_boja>p:
        raspodjela = False
        break

if raspodjela:
    print("YES")
else: 
    print("NO")
