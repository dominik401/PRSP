y = int(input("unesi godinu: "))

while True:
    y +=1
    if len(set(str(y))) == len(str(y)):
        print(y)
        break