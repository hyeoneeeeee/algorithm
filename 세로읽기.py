l=[];
for _ in range(5):
    l.append(list(str(input())))
for a in range(15):
    n=0
    while n<=5:
        try: print(l[n][a],end=""); n+=1
        except: n+=1; pass