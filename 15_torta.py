#ne daje 100% tocan ispis
n = int(input("broj testnih slucajeva: "))

for _ in range(n):
    s = int(input("broj slojeva u torti: "))
    k = list(map(int, input("količina kreme u torti: ").split()))

    result = [0] * s # ako je n=5 [0, 0, 0, 0, 0]

    ostatak_kreme = 0 

    for i in range(n -1, -1, -1):
        ostatak_kreme = max(ostatak_kreme - 1, k[i])

        if ostatak_kreme > 0:
            result[i] = 1

    print(" ".join(map(str, result)))
