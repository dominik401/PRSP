t = int(input("broj test slucajeva: "))

for _ in range(t):
    a, b = map(int, input("upisite brojeve a i b: ").split())

    razlika = abs(b-a)

    potezi = razlika // 10 + (1 if razlika % 10 != 0 else 0)

    print(potezi)