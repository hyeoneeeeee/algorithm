f=lambda:map(int, input().split())
a,b=f()
l1=[*range(1,a+1)]
for _ in range(b):
    i,j,k=f()
    l1=l1[:i-1]+l1[k-1:j]+l1[i-1:k-1]+l1[j:]
print(*l1)
