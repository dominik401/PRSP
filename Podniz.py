n = int(input())  # Broj elemenata u nizu
niz = list(map(int, input().split()))  # Unos niza brojeva

max_podniz = []
trenutni_podniz = [niz[0]]

for i in range(1, n):
    if niz[i] > niz[i-1]:
        trenutni_podniz.append(niz[i])
    else:
        if len(trenutni_podniz) > len(max_podniz):
            max_podniz = trenutni_podniz
            trenutni_podniz = [niz[i]]

if len(trenutni_podniz) > len(max_podniz):
    max_podniz=max(max_podniz, trenutni_podniz)
print(max_podniz) # max podniz
print(len(max_podniz)) # duljina max podniza
