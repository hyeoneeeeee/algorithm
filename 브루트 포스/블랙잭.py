n,m=map(int, input().split())
l=list(map(int, input().split()))
a=0
for i in l:
    for j in l:
        if i==j:
            pass
        else:
            for k in l:
                if i==k or j==k or i+j+k >m:
                    pass
                else:
                    if i+j+k>a:
                        a=i+j+k
print(a)