n = int(input("Unesite broj timova: ")) # broj timova

timovi = [] #boje dresova po timu (domaci, gostujuci)

for _ in range(n):
    hi, ai = map(int, input("Unesite boje dresova (domaci, gostujuci): ").split())
    timovi.append((hi, ai))

utakmice = 0 #broj utakmica gdje ce DOMACI morati nositi GOSTUJUCI DRES

for i in range(n):
    for j in range(n):
        if i !=j:
            if timovi[i][0] == timovi[j][1]:
                utakmice +=1
print(utakmice)