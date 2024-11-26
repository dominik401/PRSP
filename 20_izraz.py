a = int(input())
b = int(input())
c = int(input())

results = [
    a + b + c,
    a * b * c,
    a * (b + c),
    (a + b) * c,
    a + b * c,
    a * b + c
]

najveca_vrijednost= max(results)

print(results)
print("Najveca vrijednost: " +str(najveca_vrijednost))