n,m=map(int, input().split())
arr=[]
for _ in range(m):
    arr.append(list(map(int, input().split())))
else:
    for a in arr:
        x=list(map(int, input().split()))
        for b in range(n):
            a[b] = a[b]+x[b]
print(arr)
