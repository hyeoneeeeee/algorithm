n,m=map(int, input().split())
arr=[]
for _ in range(n):
    arr.append(list(map(int, input().split())))
print(arr)
for a in arr:
    x=list(map(int, input().split()))
    for b in range(m):
        a[b] = a[b]+x[b]
    print(*a)