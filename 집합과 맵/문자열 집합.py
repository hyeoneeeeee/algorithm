n, m = map(int, input().split())
sn = set(input() for _ in range(n))
a = 0
for _ in range(m):
    if input() in sn:
        a += 1
    else: pass
print(a)
