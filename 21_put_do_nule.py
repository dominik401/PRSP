t = int(input("testni slucajevi: "))
for _ in range(t):
    x, y = map(int, input().split())
    a, b = map(int, input().split())

    if a + a <= b:
        print((x+y)*a)
    else:
        print(min(x,y)*b + abs(x-y)*a)