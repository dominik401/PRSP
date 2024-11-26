n = int(input("Unesite broj zadataka: "))

zadaci = 0

for _ in range(n):
    p, v, t = map(int, input("Unesite tko je siguran u rješenje: ").split())

    if p + v + t >=2:
        zadaci +=1
    
print(zadaci)