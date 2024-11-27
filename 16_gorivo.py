n, v = map(int, input("unesi broj gradova i kapacitet za gorivo: ").split())

if v >= n-1:
    print(n-1)
else:
    cijena = v #3(u prvom gradu)
    ostatak_puta = n-v

    for i in range(2, n-ostatak_puta + 1):
        cijena +=i # 3(u prvom gradu)+2(u drugom)+3(u trecem)
    print(cijena)