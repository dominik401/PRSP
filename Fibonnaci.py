def f(unos):
    if unos <=1:
        return unos
    else:
        return f(unos-1) + f(unos-2) 
    
def f_din(unos):
    mem = [0,1]
    for i in range(2, unos+1):
        mem.append(mem[i-1]+mem[i-2])
    return(mem[unos])


def f_bez_rek(unos):
    fib=[0] *(unos+1)
    fib[1]= 1
    for i in range(2, unos+1):
        fib[i]= fib[i-1]+fib[i-2]
    print(fib[unos])

unos = int(input("unesi broj: "))

print(f(unos))
print(f_din(unos))
f_bez_rek(unos)