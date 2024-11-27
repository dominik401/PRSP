def min_distanca(n, slojevi):
    pozicije = {sloj:[0, 0] for sloj in range(1, n+1)}

    total =0
    for i, sloj in enumerate(slojevi):
        total += abs(i - pozicije[sloj][0]) + abs(i - pozicije[sloj][1])
        pozicije[sloj][0] = i
        pozicije[sloj][1] = i

    print(total)


n = int(input())
slojevi = list(map(int, input().split()))
min_distanca(n, slojevi)
