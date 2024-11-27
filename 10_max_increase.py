n = int(input("koliko je brojeva u nizu: "))

a = list(map(int, input("unos niza: ").split()))

maks = 1
trenutni = 1


for i in range(1, n):
    if a[i] > a[i-1]:
        trenutni +=1
    else:
        maks = max(maks, trenutni)
        trenutni = 1

maks= max(maks, trenutni)
print(maks)


