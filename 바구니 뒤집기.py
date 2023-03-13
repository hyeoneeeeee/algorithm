n, m = map(int, input().split(" "))
a = [a for a in range(1,n+1)]
b = []
p = 0
for _ in range(0,m):
    x,y = map(int, input().split(" "))
    b = list(reversed(a[x-1:y]))
    for g in range(x-1, y):
        a[g] = b[p]
        p += 1
    p = 0
print(*a)
