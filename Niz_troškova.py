n = int(input())  # Unos broja stubica
cijena = list(map(int, input().split()))  # Unos cijene stubica

# Polje za pohranu minimalnih troškova
dp = [0] * n

# Početni uvjeti: Za prvu i drugu stubu cijena je sama cijena stubice
dp[0] = cijena[0]
dp[1] = cijena[1]

# Izračunavanje minimalnih troškova za svaku stubu
for i in range(2, n):
    dp[i] = cijena[i] + min(dp[i-1], dp[i-2])

# Minimalna cijena za dolazak na vrh
print(min(dp[n-1], dp[n-2]))  # Ispisujemo minimalnu cijenu dolaska na vrh
