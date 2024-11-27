w = int(input("Unesi tezinu lubenice: "))
# broj mora biti: veci od dva, paran tako da ostanu 
# dva parna broja nakon dijeljenja s dva
if w >2 and w % 2==0:
    print("YES")
else:
    print("NO")