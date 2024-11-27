n = int(input("unesite iznos: "))
apoeni = [100, 20, 10, 5, 1]
novcanice = 0

for a in apoeni:
    novcanice += n // a
    n = n % a

print(novcanice)

