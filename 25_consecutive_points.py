t = int(input())
for _ in range(t):
    n = int(input())
    x = list(map(int, input().split()))
    s = set()
    for i in x:
        s.add(i - 1)
        s.add(i)
        s.add(i + 1)
    s = sorted(s)
    ok = False
    for i in range(len(s) - n + 1):
        if s[i + n - 1] - s[i] == n - 1:
            ok = True
            break
    print("YES" if ok else "NO")
