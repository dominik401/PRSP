t = int(input())
for _ in range(t):
    w, p = input(), int(input())
    s = sorted([(ord(c) - 96, i) for i, c in enumerate(w)], reverse=True)
    while sum(c[0] for c in s) > p:
        s.pop(0)
    print("".join(w[i] for _, i in sorted(s, key=lambda x: x[1])))
