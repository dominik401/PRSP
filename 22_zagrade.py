def fja(t, test_sluc):
    rez = []
    for n, s in test_sluc:
        balance = 0
        moves = 0
        for char in s:
            if char == '(':
                balance += 1
            else: # char == ')'
                if balance > 0:
                    balance -= 1
                else:
                    moves +=1
        results.append(moves)
    return results
                    
t = int(input())
test_sluc = []
for _ in range(t):
    n = int(input())
    s = input().strip()
    test_sluc.append(n, s)

results = fja(t, test_sluc)

for rez in results:
    print(rez)
