def fja(n, k, a):
    b = a[:]
    dodatne_setnje = 0
    
    for i in range(n -1):
        if b[i] + b[i+1] < k:
            potrebne_setnje = k - (b[i] + b[i +1])
            b[i + 1] += potrebne_setnje
            dodatne_setnje += potrebne_setnje
    return dodatne_setnje, b

n, k = map(int, input().split())
a = list(map(int, input().split()))

dodatne, b = fja(n, k, a)
print(dodatne)
print(' '.join(map(str, b)))
