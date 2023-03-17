a,b,c=0,0,0
for i in range(9):
    x=list(map(int, input().split()))
    for n in x:
        if c<=n: c=n; b=x.index(n)+1; a=i+1;
        elif c>n: pass
print(c)
print(a,b)
