y = int(input("unesi godinu: "))

def sve_razlicite(g):
    return len(set(str(g))) == len(str(g))

while True:
    y +=1
    if sve_razlicite(y):
        print(y)
        break