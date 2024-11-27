n = int(input())  # Broj stubišta
dp = [0] * (n + 1)  # Polje za pohranu broja načina za svaku stubu
dp[0] = 1  # Na početnoj stubi postoji samo jedan način (ne pomakni se)
dp[1] = 1  # Ako je samo jedna stubica, također postoji samo jedan način

# Izračunavanje broja načina za svaku stubu
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])  
