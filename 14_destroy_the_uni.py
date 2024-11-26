t = int(input("tesni slucajevi: "))

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if all(x==0 for x in a):
        print(0)
        continue

    jedinstvene = set(a)

    if 0 in jedinstvene:
        print(len(jedinstvene)-1)
    else:
        print(len(jedinstvene))