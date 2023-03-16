f=lambda:map(int, input().split())

a,b=f()
l=[*range(1,a+1)]
for _ in range(b):
    i,j,k=f()
    l2=l[k-1:j]
    del l[k-1:j]
    l=l2+l
    print(l2)
    print(l)
print(l)