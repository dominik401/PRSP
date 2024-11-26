t = int(input("broj testnih slucajeva: "))

for _ in range(t):
    a, b, c, x, y = map(int, input("unos slucaja(hrana za pse, hrana za macke, univerzalna hrana, broj pasa, broj macaka): ").split())
    hrana_za_pse = max(0, x - a)
    hrana_za_macke = max(0, y - b)

    if hrana_za_macke + hrana_za_macke <= c:
        print("YES")
    else:
        print("NO")
    