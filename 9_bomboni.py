n = int(input("unesite broj testnih slucajeva: "))

for _ in range(n):
    b = int(input("broj bombona: "))
    t = list(map(int,input("tezine bombona: ").split()))

    jedan = t.count(1)
    dva = t.count(2)
    ukupno = jedan + 2 * dva

    if ukupno % 2 != 0:
        print("NO")
    else:
        polovice = ukupno // 2
    
        if polovice <= dva * 2 + jedan:
            print("YES")
        else:
            print("NO")



