def f_lista(unos, apoeni, koristeni):
    if unos==0:
        return koristeni
    for a in apoeni:
        if unos>= a:
            return f_lista(unos-a, apoeni, koristeni + [a])
        
def f_brojac(unos, apoeni, brojac):
    if unos==0:
        return brojac
    for a in apoeni:
        if unos>=a:
            brojac+=1
            return f_brojac(unos-a, apoeni, brojac)

apoeni=[200, 100, 50, 20, 10, 5, 2, 1]

unos = int(input("unesi sumu: "))
rez= f_lista(unos, apoeni, [])
rez2=f_brojac(unos, apoeni, 0)
print(rez)
print(rez2)


