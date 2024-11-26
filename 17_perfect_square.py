import math
n = int(input())
niz = list(map(int, input().split()))

def savrseni_korijen(x):
    if x<0:
        return False
    korijen = int(math.sqrt(x))
    return korijen * korijen == x # uvjet za savrseni korijen

najveci_ne_kvadrat = None

for _ in niz:
    if not savrseni_korijen(_):
         if najveci_ne_kvadrat is None or _ > najveci_ne_kvadrat:
             najveci_ne_kvadrat = _

print(najveci_ne_kvadrat)
