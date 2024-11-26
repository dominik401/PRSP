def solve(n, s):
    print("funkcija")
def main():
    t = int(input("broj testnih slucajeva: "))
    rezultat=[]
    for _ in range(t):
        n = int(input("broj prijatelja: "))
        slatkisi = list(map(int, input("popis slatkisa koje imaju prijatelji: ").split()))
        rezultat.append(solve(n, slatkisi))

    print("\n".join(map(str,rezultat)))

main()